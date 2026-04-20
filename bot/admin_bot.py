import logging
import asyncio
import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from sqlalchemy import select, func

from database import init_db, AsyncSessionLocal, QuestionBank, AnswerHistory
from config import ADMIN_BOT_TOKEN, ADMIN_CHAT_ID, AWS_DOMAINS

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a detailed administrative report to the authorized chat."""
    # SECURITY: Strictly restrict to ADMIN_CHAT_ID
    if str(update.effective_chat.id) != str(ADMIN_CHAT_ID):
        logger.warning(f"Unauthorized access attempt from chat ID: {update.effective_chat.id}")
        return

    report_lines = ["🕉️ **AWS Tutor Admin Dashboard** 🕉️\n"]

    async with AsyncSessionLocal() as session:
        # 1. Vault Status (Stockpiling Progress)
        report_lines.append("🏛️ **Question Bank Status (Unused)**")
        stmt = select(
            QuestionBank.domain, 
            func.count(QuestionBank.id)
        ).where(QuestionBank.is_used == 0).group_by(QuestionBank.domain)
        
        results = await session.execute(stmt)
        stockpile_data = {domain: count for domain, count in results.all()}
        
        for domain in AWS_DOMAINS:
            count = stockpile_data.get(domain, 0)
            progress = (count / 1000) * 100
            report_lines.append(f"• {domain}: **{count}/1000** ({progress:.1f}%)")

        report_lines.append("\n📈 **User Performance (Last 7 Days)**")
        
        # 2. Daily Stats (History Aggregation)
        # Using func.date to group by day
        stmt_history = select(
            func.date(AnswerHistory.timestamp).label('day'),
            AnswerHistory.domain,
            func.count(AnswerHistory.id).label('total'),
            func.count(AnswerHistory.id).filter(AnswerHistory.is_correct == True).label('correct')
        ).group_by('day', AnswerHistory.domain).order_by('day')
        
        history_results = await session.execute(stmt_history)
        history_data = history_results.all()

        if not history_data:
            report_lines.append("_No study history recorded yet._")
        else:
            current_day = None
            for row in history_data:
                day_str = str(row.day)
                if day_str != current_day:
                    report_lines.append(f"\n📅 **{day_str}**")
                    current_day = day_str
                
                success_rate = (row.correct / row.total) * 100 if row.total > 0 else 0
                report_lines.append(f"  ▫️ {row.domain}: {row.total} ans ({success_rate:.1f}% accuracy)")

    final_report = "\n".join(report_lines)
    await update.message.reply_text(final_report, parse_mode="Markdown")

async def post_init(application) -> None:
    await init_db()
    logger.info("Admin Bot initialized.")

if __name__ == '__main__':
    if not ADMIN_BOT_TOKEN:
        logger.error("ADMIN_BOT_TOKEN not found in environment!")
        exit(1)

    application = ApplicationBuilder().token(ADMIN_BOT_TOKEN).post_init(post_init).build()
    
    application.add_handler(CommandHandler("dashboard", dashboard))
    
    logger.info("Admin Command Center starting...")
    application.run_polling()
