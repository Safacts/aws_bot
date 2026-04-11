import os
import glob
import time
from langchain_community.document_loaders import TextLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import GEMINI_API_KEY
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DOCS_DIR = "./aws_docs"
CHROMA_DIR = "./chroma_db"

def ingest_docs():
    if not os.path.exists(DOCS_DIR):
        logger.warning(f"Directory {DOCS_DIR} does not exist. Creating it.")
        os.makedirs(DOCS_DIR)
        logger.info(f"Please place text or markdown documents in {DOCS_DIR} and re-run.")
        return

    documents = []
    # Load TXT files
    for filepath in glob.glob(os.path.join(DOCS_DIR, "*.txt")):
        loader = TextLoader(filepath, encoding='utf-8')
        documents.extend(loader.load())
    
    # Load MD files
    for filepath in glob.glob(os.path.join(DOCS_DIR, "*.md")):
        loader = UnstructuredMarkdownLoader(filepath)
        documents.extend(loader.load())

    if not documents:
        logger.warning(f"No text or markdown files found in {DOCS_DIR}.")
        return

    # Chunk the docs
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    docs = text_splitter.split_documents(documents)
    logger.info(f"Split raw documents into {len(docs)} chunks.")

    # Generate Embeddings & Store in batches to respect 100 RPM limit
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", google_api_key=GEMINI_API_KEY)
    
    logger.info("Initializing Chroma DB & generating embeddings in batches of 50... This might take a bit.")
    
    BATCH_SIZE = 50
    vectorstore = None
    
    for i in range(0, len(docs), BATCH_SIZE):
        batch = docs[i : i + BATCH_SIZE]
        if i == 0:
            vectorstore = Chroma.from_documents(
                documents=batch, 
                embedding=embeddings, 
                persist_directory=CHROMA_DIR
            )
        else:
            vectorstore.add_documents(batch)
        
        logger.info(f"Processed batch {i // BATCH_SIZE + 1}. Total chunks: {min(i + BATCH_SIZE, len(docs))}")
        
        # Sleep if more batches remain
        if i + BATCH_SIZE < len(docs):
            logger.info("Sleeping for 65 seconds to respect quota...")
            time.sleep(65)

    vectorstore.persist()
    logger.info(f"Successfully ingrained {len(docs)} chunks into {CHROMA_DIR}.")

if __name__ == "__main__":
    ingest_docs()
