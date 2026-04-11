import json
import logging
import re
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
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
        self.vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=self.embeddings)
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 2}) # Top 2 chunks

        # LLMs
        self.gemini = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            google_api_key=GEMINI_API_KEY,
            temperature=0.2 # low temp for quiz precision
        )
        self.ollama = ChatOllama(
            model="llama3.2:latest", 
            base_url=OLLAMA_BASE_URL,
            temperature=0.2
        )
        
        # System prompts
        self.quiz_prompt = PromptTemplate.from_template(
            "You are an AWS Cloud Practitioner Tutor. Using ONLY the following context:\n\n{context}\n\n"
            "Generate ONE multiple-choice question for the domain: {domain}.\n"
            "You MUST output your response purely as a valid JSON object without any additional conversational text or markdown code blocks. The JSON format must be strictly:\n"
            "{{\n"
            "  \"question\": \"The exact question text?\",\n"
            "  \"options\": [\"Option 1\", \"Option 2\", \"Option 3\", \"Option 4\"],\n"
            "  \"correct_index\": <integer between 0 and 3>,\n"
            "  \"explanation\": \"Why this answer is correct.\"\n"
            "}}"
        )
        
        self.summary_prompt = PromptTemplate.from_template(
            "You are an AWS Cloud Practitioner Tutor. The user is struggling with the domain: {domain}.\n"
            "Using ONLY the following gathered context, provide a brief, simplified text summary of the key concepts for this domain.\n\n"
            "Context:\n{context}\n\n"
            "Provide the summary directly."
        )

    async def _invoke_llm(self, prompt_text: str) -> str:
        """Invokes Gemini first, falling back to Ollama if rate limits or network issues occur."""
        try:
            logger.info("Attempting inference with Gemini...")
            response = await self.gemini.ainvoke(prompt_text)
            return response.content
        except EXHAUSTED_EXC as e:
            logger.warning(f"Google API rate limit (ResourceExhausted) hit: {e}. Falling back to Ollama.")
            response = await self.ollama.ainvoke(prompt_text)
            return response.content
        except Exception as e:
            # Broad catch-all for other Google API connection issues
            if "exhausted" in str(e).lower() or "quota" in str(e).lower() or "rate" in str(e).lower():
                logger.warning(f"Google API rate limit hit: {e}. Falling back to Ollama.")
                response = await self.ollama.ainvoke(prompt_text)
                return response.content
            # Re-raise if it isn't clearly a connection/quota issue assuming we only fallback on specific errors
            # But the user said: "If Gemini throws a rate limit or network exception" so catching all is safer
            logger.warning(f"Google API exception: {e}. Falling back to Ollama.")
            response = await self.ollama.ainvoke(prompt_text)
            return response.content

    async def generate_question(self, domain: str) -> Dict[str, Any]:
        """Runs RAG, prompts LLM, and parses back the question JSON."""
        docs = self.retriever.invoke(domain)
        context = "\n\n".join([d.page_content for d in docs])
        
        prompt_text = self.quiz_prompt.format(domain=domain, context=context)
        
        raw_output = await self._invoke_llm(prompt_text)
        clean_json = clean_json_string(raw_output)
        
        try:
            return json.loads(clean_json)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM JSON output: {clean_json}")
            raise Exception("LLM returned malformed JSON") from e

    async def generate_summary(self, domain: str) -> str:
        """Runs RAG, queries LLM context for a simplified domain summary."""
        docs = self.retriever.invoke(domain)
        context = "\n\n".join([d.page_content for d in docs])
        
        prompt_text = self.summary_prompt.format(domain=domain, context=context)
        return await self._invoke_llm(prompt_text)

# Singleton instance
rag_router = HybridRAGRouter()
