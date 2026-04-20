import json
import logging
import re
import random
import uuid
from typing import Dict, Any


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma



from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


from config import GEMINI_API_KEY, GROQ_API_KEY



logger = logging.getLogger(__name__)

# Try to import the specific exception; fallback to general Exception if not available
try:
    from google.api_core.exceptions import ResourceExhausted
    EXHAUSTED_EXC = ResourceExhausted
except ImportError:
    EXHAUSTED_EXC = Exception

def clean_json_string(raw: str) -> str:
    """Extracts JSON block from text, handling markdown fences and garbage."""
    raw = raw.strip()
    if "```" in raw:
        # Remove markdown fences regardless of language label
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("`").strip()
    
    # Locate the first '{' and the last '}'
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end != -1 and end > start:
        return raw[start:end + 1]
    return raw



class HybridRAGRouter:
    def __init__(self):
        # Set up Embeddings and Vector Store
        # Using standard model naming; local chroma_db dir must exist
        self.embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", google_api_key=GEMINI_API_KEY)
        self.vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=self.embeddings)
        # Fetching more chunks to allow for randomization later
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 10})

        # Primary LLM (Local Ollama llama3)
        self.primary_llm = ChatOllama(
            base_url="http://sakhi_engine:11434",
            model="llama3",
            temperature=0.8,
            format="json"
        )
        
        # Fallback LLM (Groq Llama-3.3-70B)
        self.fallback_llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0.8,
            max_tokens=1024
        )
        
        # Legacy placeholder (removed direct self.llm usage)
        self.llm = self.primary_llm









        
        # System prompts (AWS Sensei Persona)
        self.quiz_prompt = PromptTemplate.from_template(
            "You are the 'AWS Sensei', a world-class AWS instructor and mentor for Jeevitha.\n"
            "CRITICAL: You are an API. Your response must contain NOTHING except the JSON block. "
            "Do not include greetings or names outside of the JSON. If you include any text outside the curly braces, the system will crash.\n\n"
            "Task: Generate ONE high-fidelity, scenario-based multiple-choice question for the domain: {domain}.\n\n"
            "STRICT GENERATION RULES:\n"
            "1. NO TRIVIA: Do NOT ask 'What is X?' Ask: 'A company has [Scenario]. They need [Requirement]. Which service is best?'\n"
            "2. TECHNICAL RIGOR: Ensure absolute accuracy for CLF-C02 standards.\n"
            "3. INDUSTRY ROTATION: Pick a scenario: FinTech, Healthcare, Gaming, E-commerce, or Government.\n"
            "4. PLAUSIBLE DISTRACTORS: Use real AWS services that are relevant but wrong for the scenario.\n\n"
            "FORMAT & PERSONA:\n"
            "- The 'explanation' field must start with a personalized mentorship sentence for Jeevitha (e.g., 'A great choice, Jeevitha...' or 'Focus on the requirement, Jeevitha...'), followed by a detailed architectural explanation.\n"
            "- Do NOT include the persona in any other part of the JSON.\n\n"
            "CRITICAL: The `question` string MUST be UNDER 250 CHARACTERS.\n"
            "Input Random Seed: {seed}\n\n"
            "Output response ONLY as valid JSON:\n"
            "{{\n"
            "  \"question\": \"...\",\n"
            "  \"options\": [\"...\", \"...\", \"...\", \"...\"],\n"
            "  \"correct_index\": <0-3>,\n"
            "  \"explanation\": \"...\"\n"
            "}}"
        )








        self.summary_prompt = PromptTemplate.from_template(
            "GREETING (Sensei): Encourage Jeevitha and acknowledge her progress in the {domain} domain.\n"
            "TECHNICAL (Expert): Provide a professional, bulleted summary of the core {domain} facts from the context.\n\n"
            "Context:\n{context}\n"
        )




    async def _invoke_llm(self, messages: list) -> str:
        """Invokes local Ollama with a fallback to Groq."""
        # Hardcode even stricter JSON instructions for llama3 reliability
        system_instruction = (
            "You are a JSON API. You output ONLY a valid JSON object. "
            "You never write any text before or after the JSON. You never use markdown. "
            "Your entire response is always a single JSON object starting with { and ending with }."
        )
        
        # Override the system message if it's the default question generator
        if isinstance(messages[0], SystemMessage):
            messages[0].content = system_instruction

        try:
            logger.info("Attempting inference with local Ollama (llama3)...")
            response = await self.primary_llm.ainvoke(messages)
            return response.content
        except Exception as e:
            logger.warning(f"Ollama failed ({e}), falling back to Groq...")
            response = await self.fallback_llm.ainvoke(messages)
            return response.content








    async def generate_question(self, domain: str) -> Dict[str, Any]:
        """Orchestrates RAG retrieval and question generation with shuffle-and-sample fail-safes."""
        context = ""
        try:
            # 1. Retrieve top 10 chunks
            all_docs = self.retriever.invoke(domain)
            
            # 2. Shuffle and pick top 3 for variety
            random.shuffle(all_docs)
            selected_docs = all_docs[:3]
            
            context = "\n\n".join([d.page_content for d in selected_docs])
            logger.info(f"Sampled 3/10 random chunks for {domain}.")
        except Exception as rag_err:
            logger.error(f"RAG Retrieval failed: {rag_err}. Proceeding with internal knowledge.")
            context = "NO DOCUMENTATION CONTEXT AVAILABLE."

        # 3. Generate content using LLM (with its own fallback)
        seed = str(uuid.uuid4())
        prompt_text = self.quiz_prompt.format(domain=domain, context=context, seed=seed)
        
        messages = [
            SystemMessage(content="You are an AWS exam question generator. Output JSON only."),
            HumanMessage(content=prompt_text)
        ]
        raw_output = await self._invoke_llm(messages)

        
        # 4. Final parsing
        raw_output = raw_output.strip()
        clean_json = clean_json_string(raw_output)

        try:
            data = json.loads(clean_json)
            
            # --- VALIDATION & CLAMPING (Fix 3) ---
            # Truncate strings to stay within Telegram Poll limits
            data["options"] = [str(o)[:99] for o in data["options"]]
            data["question"] = str(data["question"])[:299]
            
            # Integrity checks
            if len(data["options"]) != 4:
                raise ValueError("Expected 4 options")
            if not isinstance(data.get("correct_index"), int) or not (0 <= data["correct_index"] <= 3):
                raise ValueError("Invalid correct_index")
                
            return data
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            logger.error(f"JSON Output Parsing/Validation Error: {e}")
            logger.error(f"RAW LLM OUTPUT (FAILED PARSE): {raw_output}")
            raise






    async def generate_summary(self, domain: str) -> str:
        """Generates a topic summary with RAG and LLM fail-safes."""
        context = ""
        try:
            docs = self.retriever.invoke(domain)
            context = "\n\n".join([d.page_content for d in docs])
        except Exception:
            context = "General knowledge summary."

        prompt_text = self.summary_prompt.format(domain=domain, context=context)
        system_instruction = "You are a professional AWS Solutions Architect and expert instructor."
        return await self._invoke_llm(prompt_text, system_instruction=system_instruction)




# Singleton instance
rag_router = HybridRAGRouter()
