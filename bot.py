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

async def ask_next_question(chat_id: int, user_id: int, context: ContextTypes.DEFAULT_TYPE, retry_count: int = 0):
    """Fetches a generated question and sends it to the user with retry logic."""
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
        explanation = question_data.get("explanation", "No explanation provided.")
        
        # Send Poll (Explicitly NON-ANONYMOUS and without native explanation to bypass 200 char limit)
        poll_message = await context.bot.send_poll(
            chat_id=chat_id,
            question=question_data["question"],
            options=question_data["options"],
            type="quiz",
            correct_option_id=question_data["correct_index"],
            is_anonymous=False
        )
        
        # Track the active poll and store explanation/chat_id for later delivery
        context.bot_data[poll_message.poll.id] = {
            "explanation": explanation,
            "user_id": user_id,
            "chat_id": chat_id,
            "correct_option_id": question_data["correct_index"]
        }
        
        # Delete processing message
        await context.bot.delete_message(chat_id=chat_id, message_id=processing_msg.message_id)
        
        # Update user stat (question asked)
        user.questions_asked += 1
        await save_user(user)

    except Exception as e:
        logger.error(f"Error generating question (Attempt {retry_count + 1}): {e}")
        
        if retry_count < 1:
            await context.bot.edit_message_text(
                chat_id=chat_id, 
                message_id=processing_msg.message_id, 
                text="⚠️ Gemini is busy. Retrying in 3 seconds... ⏳"
            )
            import asyncio
            await asyncio.sleep(3)
            # Delete old processing message and try again
            await context.bot.delete_message(chat_id=chat_id, message_id=processing_msg.message_id)
            return await ask_next_question(chat_id, user_id, context, retry_count=retry_count + 1)
        else:
            await context.bot.edit_message_text(
                chat_id=chat_id, 
                message_id=processing_msg.message_id, 
                text="⚠️ Sorry, there was an issue generating the question after retries. Please type /start to try again."
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
    """Handles incoming poll answers and triggers the infinite learning loop."""
    answer = update.poll_answer
    poll_id = answer.poll_id
    
    stored_data = context.bot_data.get(poll_id)
    if not stored_data:
        return
        
    user_id = answer.user.id
    chat_id = stored_data.get("chat_id", user_id) # Fallback to user_id for private chats
    explanation = stored_data.get("explanation", "No explanation available.")
    selected_option = answer.option_ids[0]
    is_correct = (selected_option == stored_data["correct_option_id"])
    
    user = await get_or_create_user(user_id)
    
    # Cleanup and send explanation
    if poll_id in context.bot_data:
        del context.bot_data[poll_id]
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"💡 **Explanation:**\n{explanation}",
        parse_mode="Markdown"
    )

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
            current_domain = "Unknown"
            if user.current_topic_index < len(AWS_DOMAINS):
                current_domain = AWS_DOMAINS[user.current_topic_index]
            
            user.current_wrong_streak = 0 
            
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

    # Update state and trigger next question automatically
    await save_user(user)
    
    # Wait briefly before firing next question to ensure UX flow
    import asyncio
    await asyncio.sleep(2)
    await ask_next_question(chat_id, user_id, context)


async def next_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manually advances the user to the next AWS domain."""
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    user = await get_or_create_user(user_id)
    
    # Increment and wrap around
    user.current_topic_index = (user.current_topic_index + 1) % len(AWS_DOMAINS)
    user.current_correct_streak = 0
    user.current_wrong_streak = 0
    
    await save_user(user)
    
    new_domain = AWS_DOMAINS[user.current_topic_index]
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"⏩ **Skipping to next topic:** {new_domain}",
        parse_mode="Markdown"
    )
    
    await ask_next_question(chat_id, user_id, context)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update:", exc_info=context.error)
    if isinstance(update, Update) and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ An internal error occurred. Our engineers have been notified. Please try again later."
        )

async def post_init(application) -> None:
    """Initializes the database within the application's event loop."""
    await init_db()
    logger.info("Database initialization complete in post_init.")

if __name__ == '__main__':
    # Build Telegram App with post_init hook
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    
    # Track polls in bot_data memory
    if "bot_data" not in application.bot_data:
        application.bot_data = {}

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('next', next_topic))
    application.add_handler(PollHandler(receive_poll_answer))
    application.add_error_handler(error_handler)
    
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

