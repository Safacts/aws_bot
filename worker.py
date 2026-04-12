import asyncio
import logging
import json
from sqlalchemy import select, func
from database import AsyncSessionLocal, QuestionBank, init_db
from rag_router import rag_router
from config import AWS_DOMAINS

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def pregenerate_questions():
    """Background loop to pre-generate questions for each domain."""
    logger.info("Worker: Starting background generator...")
    await init_db()
    
    while True:
        for domain in AWS_DOMAINS:
            try:
                async with AsyncSessionLocal() as session:
                    # Check how many unused questions we have
                    stmt = select(func.count()).select_from(QuestionBank).where(
                        QuestionBank.domain == domain,
                        QuestionBank.is_used == 0
                    )
                    result = await session.execute(stmt)
                    count = result.scalar()
                    
                    if count < 5:
                        logger.info(f"Worker: Level low for '{domain}' ({count}/5). Generating with local Ollama...")
                        question_data = await rag_router.generate_question_ollama(domain)
                        
                        new_q = QuestionBank(
                            domain=domain,
                            question_data=json.dumps(question_data),
                            is_used=0
                        )
                        session.add(new_q)
                        await session.commit()
                        logger.info(f"Worker: Successfully added question for '{domain}'.")
                    else:
                        logger.info(f"Worker: Sufficient stock for '{domain}' ({count}). Skipping.")
            except Exception as e:
                logger.error(f"Worker error during generation for {domain}: {e}")
            
            # Pacing removed as requested to allow faster generation via local LLM
            await asyncio.sleep(0.1) 



if __name__ == "__main__":
    try:
        asyncio.run(pregenerate_questions())
    except KeyboardInterrupt:
        logger.info("Worker stopped manually.")
