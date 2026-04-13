import asyncio
import json
import logging
from sqlalchemy import select, func
from database import AsyncSessionLocal, QuestionBank, init_db
from rag_router import rag_router
from config import AWS_DOMAINS

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants (Logic from user request)
STOCKPILE_TARGET = 100
SLEEP_BETWEEN_GENERATIONS = 1   # Local Ollama has no rate limit
SLEEP_ON_ERROR = 10              # seconds — short retry on parse errors
SLEEP_ON_RATE_LIMIT = 60        # seconds — back off on 429

async def get_stock(domain: str) -> int:
    """Async safely counts unused questions for a domain."""
    async with AsyncSessionLocal() as session:
        stmt = select(func.count()).select_from(QuestionBank).where(
            QuestionBank.domain == domain,
            QuestionBank.is_used == 0
        )
        result = await session.execute(stmt)
        return result.scalar()

async def run_worker():
    """Background loop to pre-generate questions with sequential priority."""
    logger.info("Worker: Starting background generator (Async Priority Sweep)...")
    await init_db()

    while True:
        generated_any = False

        for domain in AWS_DOMAINS:
            stock = await get_stock(domain)

            if stock >= STOCKPILE_TARGET:
                logger.debug(f"Worker: {domain} has {stock}/{STOCKPILE_TARGET}. Skipping.")
                continue

            logger.info(f"Worker: [{domain}] needs questions ({stock}/{STOCKPILE_TARGET}). Generating...")

            try:
                question_data = await rag_router.generate_question(domain)

                async with AsyncSessionLocal() as session:
                    entry = QuestionBank(
                        domain=domain,
                        question_data=json.dumps(question_data),
                        is_used=0
                    )
                    session.add(entry)
                    await session.commit()

                logger.info(f"Worker: ✅ Added question for '{domain}'. Bank now ~{stock + 1}/{STOCKPILE_TARGET}.")
                generated_any = True
                await asyncio.sleep(SLEEP_BETWEEN_GENERATIONS)
                
                # Sequential Priority Switch: Immediately restart from Domain 1
                break 

            except Exception as e:
                err_str = str(e).lower()
                if "429" in err_str or "rate limit" in err_str or "quota" in err_str:
                    logger.warning(f"Worker: ⏳ Rate limited on '{domain}'. Sleeping {SLEEP_ON_RATE_LIMIT}s...")
                    await asyncio.sleep(SLEEP_ON_RATE_LIMIT)
                else:
                    logger.warning(f"Worker: ⚠️ Generation error for '{domain}': {e}. Retrying in {SLEEP_ON_ERROR}s...")
                    await asyncio.sleep(SLEEP_ON_ERROR)
                
                # Restart priority loop even on error to re-assess priority
                break

        if not generated_any:
            # All domains are full — sleep longer to avoid busy-spinning
            stocks_info = {}
            for d in AWS_DOMAINS:
                stocks_info[d] = await get_stock(d)
                
            logger.info(f"Worker: All domains at target (100). Stocks: {stocks_info}. Sleeping 30s...")
            await asyncio.sleep(30)

if __name__ == "__main__":
    try:
        asyncio.run(run_worker())
    except KeyboardInterrupt:
        logger.info("Worker stopped manually.")
