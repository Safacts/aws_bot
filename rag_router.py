import json
import logging
import re
import random
from typing import Dict, Any

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from config import GEMINI_API_KEY, OLLAMA_BASE_URL

logger = logging.getLogger(__name__)

# Try to import the specific exception; fallback to general Exception if not available
try:
    from google.api_core.exceptions import ResourceExhausted
    EXHAUSTED_EXC = ResourceExhausted
except ImportError:
    EXHAUSTED_EXC = Exception

def clean_json_string(raw_text: str) -> str:
    """Removes markdown block formatting and conversational filler to return clean JSON."""
    raw_text = raw_text.strip()
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

        # LLMs
        self.gemini = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite", 
            google_api_key=GEMINI_API_KEY,
            temperature=0.8
        )




        self.ollama = ChatOllama(
            model="llama3.2:latest", 
            base_url=OLLAMA_BASE_URL,
            temperature=0.8
        )
        
        # System prompts (Krishna Persona)
        # System prompts (Krishna Persona with Technical Rigor)
        self.quiz_prompt = PromptTemplate.from_template(
            "You are a professional AWS Solutions Architect generating certification questions. "
            "Task: Generate ONE multiple-choice quiz question for the domain: {domain}.\n"
            "CRITICAL: The `question` string MUST be concise and UNDER 250 CHARACTERS. "
            "DO NOT include any spiritual metaphors, Krishna persona, or analogies in the 'question' text or the 'options' strings.\n\n"
            "Output response ONLY as a valid JSON object:\n"
            "{{\n"
            "  \"question\": \"...\",\n"
            "  \"options\": [\"...\", \"...\", \"...\", \"...\"],\n"
            "  \"correct_index\": <0-3>,\n"
            "  \"explanation\": \"[Sentence 1: Brief, warm greeting and encouragement in the persona of Lord Krishna targeting 'Partha']. [Sentence 2+: Strictly professional, dry AWS technical explanation of the correct answer and why distractors are wrong. No metaphors.] CRITICAL: Do NOT write 'GREETING:' or 'TECHNICAL:' in the text.\"\n"
            "}}"
        )




        self.summary_prompt = PromptTemplate.from_template(
            "GREETING (Krishna): Greet Partha and acknowledge their effort in the {domain} domain.\n"
            "TECHNICAL (AWS Architect): Provide a 100% professional, dry, bulleted summary of the core {domain} facts from the context. No metaphors or spiritual analogies.\n\n"
            "Context:\n{context}\n"
        )




    async def _invoke_with_fallback(self, prompt_text: str) -> str:
        """Invokes Gemini primarily, with seamless fallback to local Ollama."""
        try:
            logger.info("Attempting inference with Gemini (gemini-2.5-flash-lite)...")


            response = await self.gemini.ainvoke(prompt_text)
            return response.content
        except EXHAUSTED_EXC as e:
            logger.warning(f"Gemini API Quota Exhausted (429): {e}. Switching to local Ollama.")
            return await self._invoke_ollama(prompt_text)
        except Exception as e:
            logger.warning(f"Primary LLM (Gemini) failed: {e}. Falling back to Ollama.")
            return await self._invoke_ollama(prompt_text)

    async def _invoke_ollama(self, prompt_text: str) -> str:
        """Helper to invoke local Ollama LLM."""
        try:
            logger.info("Attempting inference with local Ollama (llama3.2)...")
            response = await self.ollama.ainvoke(prompt_text)
            return response.content
        except Exception as ollama_err:
            logger.error(f"Critical Failure: Both Gemini and Ollama are offline. {ollama_err}")
            raise


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
        prompt_text = self.quiz_prompt.format(domain=domain, context=context)
        raw_output = await self._invoke_with_fallback(prompt_text)
        
        # 4. Final parsing
        clean_json = clean_json_string(raw_output)
        try:
            return json.loads(clean_json)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Output Parsing Error: {e}")
            raise

    async def generate_question_ollama(self, domain: str) -> Dict[str, Any]:
        """Worker-only direct local generation to bypass Google API/Gemini limits entirely."""
        context = ""
        try:
            all_docs = self.retriever.invoke(domain)
            random.shuffle(all_docs)
            selected_docs = all_docs[:3]
            context = "\n\n".join([d.page_content for d in selected_docs])
        except Exception:
            context = "NO DOCUMENTATION CONTEXT AVAILABLE."

        prompt_text = self.quiz_prompt.format(domain=domain, context=context)
        raw_output = await self._invoke_ollama(prompt_text)
        
        clean_json = clean_json_string(raw_output)
        try:
            return json.loads(clean_json)
        except json.JSONDecodeError as e:
            logger.error(f"Ollama Question Error: {e}")
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
        return await self._invoke_with_fallback(prompt_text)

# Singleton instance
rag_router = HybridRAGRouter()
