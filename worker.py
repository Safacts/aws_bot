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
        any_work_done = False
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
                    
                    if count < 1000:
                        try:
                            logger.info(f"Worker: Priority set to '{domain}' ({count}/1000). Generating with Gemini...")
                            question_data = await rag_router.generate_question(domain)
                            
                            new_q = QuestionBank(
                                domain=domain,
                                question_data=json.dumps(question_data),
                                is_used=0
                            )
                            session.add(new_q)
                            await session.commit()
                            logger.info(f"Worker: Successfully added question for '{domain}'.")
                            
                            # Sequential Lock: Immediately break to restart from Domain 1
                            any_work_done = True
                            await asyncio.sleep(6) # 10 RPM pacing
                            break
                        except Exception as e:
                            err_msg = str(e).lower()
                            if "429" in err_msg or "exhausted" in err_msg:
                                logger.warning("🛑 Quota Exhausted (429)! Sleeping for 1 hour to cool down...")
                                await asyncio.sleep(3600)
                            else:
                                logger.warning(f"⚠️ Worker generation skipped due to error: {e}")
                                await asyncio.sleep(6)
                            
                            await session.rollback()
                            any_work_done = True # We tried, so we break to restart
                            break
            except Exception as outer_e:
                logger.error(f"Worker: Critical session error for {domain}: {outer_e}")
                await asyncio.sleep(10)
                any_work_done = True
                break
        
        if not any_work_done:
            # If we went through all domains and none were < 1000
            logger.info("✅ All domains have 1000+ questions. Sleeping for 1 hour before next sweep.")
            await asyncio.sleep(3600)



            
            # No delay—maximizing local hardware speed as requested



if __name__ == "__main__":
    try:
        asyncio.run(pregenerate_questions())
    except KeyboardInterrupt:
        logger.info("Worker stopped manually.")
