import logging
import json
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    PollHandler,
    ContextTypes
)

from config import BOT_TOKEN, AWS_DOMAINS, STREAK_TARGET, WRONG_TARGET
from database import init_db, get_or_create_user, save_user
from rag_router import rag_router

# Set up basic logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def ask_next_question(chat_id: int, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    """Fetches a generated question and sends it to the user."""
    # Retrieve user state
    user = await get_or_create_user(user_id)
    
    # Check if they exhausted the curriculum
    if user.current_topic_index >= len(AWS_DOMAINS):
        await context.bot.send_message(
            chat_id=chat_id,
            text="🎉 Congratulations! You have mastered all the AWS Cloud Practitioner domains in our curriculum."
        )
        return
    
    current_domain = AWS_DOMAINS[user.current_topic_index]
    
    # Inform user we are generating
    processing_msg = await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🧠 Generating a question for *{current_domain}*...", 
        parse_mode="Markdown"
    )

    try:
        # LLM RAG Question Generation
        question_data = await rag_router.generate_question(current_domain)
        
        # Send Poll
        poll_message = await context.bot.send_poll(
            chat_id=chat_id,
            question=question_data["question"],
            options=question_data["options"],
            type="quiz",
            correct_option_id=question_data["correct_index"],
            explanation=question_data.get("explanation", "No explanation provided."),
            is_anonymous=False
        )
        
        # Track the active poll
        context.bot_data[poll_message.poll.id] = {
            "chat_id": chat_id,
            "user_id": user_id,
            "correct_option_id": question_data["correct_index"]
        }
        
        # Delete processing message
        await context.bot.delete_message(chat_id=chat_id, message_id=processing_msg.message_id)
        
        # Update user stat (question asked)
        user.questions_asked += 1
        await save_user(user)

    except Exception as e:
        logger.error(f"Error generating question: {e}")
        await context.bot.edit_message_text(
            chat_id=chat_id, 
            message_id=processing_msg.message_id, 
            text="⚠️ Sorry, there was an issue generating the question. Please try again later or type /start."
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Init DB user profile
    await get_or_create_user(user.id)
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Welcome to the Adaptive AWS Cloud Practitioner Tutor! ☁️\n\n"
            "I will guide you through the official AWS domains using adaptive questioning.\n"
            f"If you answer {STREAK_TARGET} correctly in a row, you advance.\n"
            f"If you miss {WRONG_TARGET} in a row, I'll provide a simplified summary of the topic to help you out.\n\n"
            "Let's get started!"
        )
    )
    
    # Send first question
    await ask_next_question(chat_id, user.id, context)

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles incoming poll answers to update adaptive logic."""
    answer = update.poll_answer
    poll_id = answer.poll_id
    
    poll_data = context.bot_data.get(poll_id)
    if not poll_data:
        # Unknown poll
        return
        
    user_id = answer.user.id
    chat_id = poll_data["chat_id"]
    selected_option = answer.option_ids[0]
    is_correct = (selected_option == poll_data["correct_option_id"])
    
    user = await get_or_create_user(user_id)
    
    # Cleanup dictionary to save memory
    del context.bot_data[poll_id]

    if is_correct:
        user.correct_answers += 1
        user.current_correct_streak += 1
        user.current_wrong_streak = 0
        
        # Level up condition
        if user.current_correct_streak >= STREAK_TARGET:
            user.current_topic_index += 1
            user.current_correct_streak = 0
            
            await context.bot.send_message(
                chat_id=chat_id,
                text="🌟 **Level Up!** 🌟\nYou've mastered this domain! Moving on to the next topic."
            )
            await save_user(user)
            await ask_next_question(chat_id, user_id, context)
            return
            
    else:
        user.current_wrong_streak += 1
        user.current_correct_streak = 0
        
        # Summary helper condition
        if user.current_wrong_streak >= WRONG_TARGET:
            current_domain = AWS_DOMAINS[user.current_topic_index]
            user.current_wrong_streak = 0 # Reset wrong streak after helping
            
            await context.bot.send_message(
                chat_id=chat_id,
                text="It looks like you're struggling a bit with this topic. Let me summarize it for you..."
            )
            
            try:
                summary = await rag_router.generate_summary(current_domain)
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"📚 **{current_domain} Summary**:\n\n{summary}",
                    parse_mode="Markdown"
                )
            except Exception as e:
                logger.error(f"Error generating summary: {e}")
                
            await save_user(user)
            await ask_next_question(chat_id, user_id, context)
            return

    await save_user(user)
    
    # In all normal scenarios (didn't level up, didn't trigger help limit), just ask the next question
    # wait a slight moment so the user reads the explanation inside the poll before spamming
    import asyncio
    context.application.create_task(
        asyncio.sleep(3), 
        name=f"delay_next_q_{user_id}"
    )
    # Wait asynchronously before firing next
    await asyncio.sleep(2)
    await ask_next_question(chat_id, user_id, context)

if __name__ == '__main__':
    import asyncio
    
    # Initialize DB schema before Bot polling starts
    asyncio.run(init_db())
    
    # Build Telegram App
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Track polls in bot_data memory
    if "bot_data" not in application.bot_data:
        application.bot_data = {}

    application.add_handler(CommandHandler('start', start))
    application.add_handler(PollHandler(receive_poll_answer))
    
    logger.info("Starting bot...")
    application.run_polling()
