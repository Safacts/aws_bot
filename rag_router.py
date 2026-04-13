import json
import logging
import re
import random
import uuid
from typing import Dict, Any


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma


from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from config import GEMINI_API_KEY, GROQ_API_KEY



logger = logging.getLogger(__name__)

# Try to import the specific exception; fallback to general Exception if not available
try:
    from google.api_core.exceptions import ResourceExhausted
    EXHAUSTED_EXC = ResourceExhausted
except ImportError:
    EXHAUSTED_EXC = Exception

def clean_json_string(raw_text: str) -> str:
    """Uses regex to extract the first valid JSON object from the LLM output."""
    raw_text = raw_text.strip()
    
    # Use re.search to find the first '{' and last '}'
    match = re.search(r'(\{.*\})', raw_text, re.DOTALL)
    if match:
        return match.group(0).strip()
    
    # Fallback to simple stripping if regex fails
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    elif raw_text.startswith("```"):
        raw_text = raw_text[3:]
        
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
        
    return raw_text.strip()


class HybridRAGRouter:
    def __init__(self):
        # Set up Embeddings and Vector Store
        # Using standard model naming; local chroma_db dir must exist
        self.embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", google_api_key=GEMINI_API_KEY)
        self.vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=self.embeddings)
        # Fetching more chunks to allow for randomization later
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 10})

        # LLM (Groq Llama-3.3-70B)
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0.7
        )








        
        # System prompts (Krishna Persona)
        # System prompts (Krishna Persona with Technical Rigor)
        self.quiz_prompt = PromptTemplate.from_template(
            "You are a professional Principal AWS Solutions Architect. "
            "Task: Generate ONE high-fidelity, scenario-based multiple-choice question for the CLF-C02 exam in the domain: {domain}.\n\n"
            "STRICT TECHNICAL RULES:\n"
            "1. INDUSTRY ROTATION: You MUST pick a specific industry for the scenario: Healthcare (PCI/HIPAA focus), Financial Services (Compliance/Resiliency), E-commerce (Scaling/Availability), Gaming (Low Latency/Global Infrastructure), or Government/Public Sector (Governance).\n"
            "2. TOPIC FOCUS: Avoid basic vocabulary. Focus on: Shared Responsibility Model, Well-Architected Framework Pillars, S3 Storage Class transitions, Edge Locations vs. Regions, or AWS Support Plan comparisons.\n"
            "3. ACCURACY: NEVER mention 'Elastic Transcoder' (use 'AWS Elemental MediaConvert'). NEVER suggest Lambda for GPU/Long-running tasks. Use precise Free Tier facts (e.g., 750 hours/month).\n"
            "4. FORMAT: Use 'Scenario -> Requirement -> Question'. Create 4 plausible options. 'correct_index' (0-3) must be 100% accurate.\n"
            "5. NO LABELS: Do NOT use literal labels like 'GREETING:' or 'TECHNICAL:'.\n\n"
            "PERSONA & EXPLANATION:\n"
            "- First Sentence: Brief, warm encouragement as Lord Krishna addressing 'Partha'.\n"
            "- Subsequent Sentences: Seamlessly transition to a cold, professional AWS architect. Provide a dry, fact-heavy breakdown of the correct choice and why distractors are insufficient.\n\n"
            "CRITICAL: The `question` string MUST be concise and UNDER 250 CHARACTERS. "
            "Input Random Seed (Unique per request): {seed}\n\n"
            "Output response ONLY as a valid JSON object:\n"
            "{{\n"
            "  \"question\": \"...\",\n"
            "  \"options\": [\"...\", \"...\", \"...\", \"...\"],\n"
            "  \"correct_index\": <0-3>,\n"
            "  \"explanation\": \"...\"\n"
            "}}"
        )






        self.summary_prompt = PromptTemplate.from_template(
            "GREETING (Krishna): Greet Partha and acknowledge their effort in the {domain} domain.\n"
            "TECHNICAL (AWS Architect): Provide a 100% professional, dry, bulleted summary of the core {domain} facts from the context. No metaphors or spiritual analogies.\n\n"
            "Context:\n{context}\n"
        )




    async def _invoke_llm(self, prompt_text: str) -> str:
        """Invokes Groq LLM primarily."""
        logger.info("Attempting inference with Groq (llama-3.3-70b-versatile)...")
        response = await self.llm.ainvoke(prompt_text)
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
        raw_output = await self._invoke_llm(prompt_text)



        
        # 4. Final parsing
        clean_json = clean_json_string(raw_output)
        try:
            return json.loads(clean_json)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Output Parsing Error: {e}")
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
        return await self._invoke_llm(prompt_text)



# Singleton instance
rag_router = HybridRAGRouter()
