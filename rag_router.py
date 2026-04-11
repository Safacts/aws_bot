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
            model="gemini-2.5-flash", 
            google_api_key=GEMINI_API_KEY,
            temperature=0.8
        )
        self.ollama = ChatOllama(
            model="llama3.2:latest", 
            base_url=OLLAMA_BASE_URL,
            temperature=0.8
        )
        
        # System prompts
        self.quiz_prompt = PromptTemplate.from_template(
            "You are a Senior AWS Lead Architect and Tutor for the AWS Certified Cloud Practitioner (CLF-C02) exam. "
            "Context from curriculum documentation:\n{context}\n\n"
            "Task: Generate ONE multiple-choice quiz question for the domain: {domain}.\n"
            "CRITICAL: Telegram limits poll questions to 300 characters. The `question` string MUST be concise, direct, and STRICTLY UNDER 250 CHARACTERS. Distractor answers should also be kept short.\n"
            "CRITICAL CONSTRAINTS:\n"
            "1. DIFFICULTY: The question MUST match the exact difficulty and trickiness of the real CLF-C02 exam.\n"
            "2. DISTRACTORS: Use high-quality, plausible distractors. Avoid obviously wrong answers. Incorrect options should look nearly correct to someone who hasn't fully mastered the concept.\n"
            "3. RANDOMIZATION: Select a RANDOM concept or scenario from the provided context chunks. DO NOT repeat the same obvious concepts. Search for nuanced details in the context.\n"
            "4. NO CONTEXT: If the context is empty, use your vast internal knowledge to create a professional CLF-C02 question.\n\n"
            "Output response ONLY as a valid JSON object:\n"
            "{{\n"
            "  \"question\": \"...\",\n"
            "  \"options\": [\"...\", \"...\", \"...\", \"...\"],\n"
            "  \"correct_index\": <0-3>,\n"
            "  \"explanation\": \"Provide a detailed, expert-level explanation of why the correct answer is right and why the distractors are wrong.\"\n"
            "}}"
        )
        
        self.summary_prompt = PromptTemplate.from_template(
            "Simplify this AWS domain for a beginner: {domain}.\n"
            "Context:\n{context}\n\n"
            "Provide a clear, brief conceptual summary."
        )

    async def _invoke_with_fallback(self, prompt_text: str) -> str:
        """Invokes Gemini primarily, with seamless fallback to local Ollama."""
        try:
            logger.info("Attempting inference with Gemini (flash-latest)...")
            response = await self.gemini.ainvoke(prompt_text)
            return response.content
        except Exception as e:
            logger.warning(f"Primary LLM (Gemini) failed: {e}. Falling back to Ollama.")
            try:
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
