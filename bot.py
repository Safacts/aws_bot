import logging
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    PollAnswerHandler,
    CallbackQueryHandler,
    ContextTypes
)


import json
import telegram.error
from sqlalchemy import select
from config import BOT_TOKEN, AWS_DOMAINS, STREAK_TARGET, WRONG_TARGET

from database import init_db, get_or_create_user, save_user, AsyncSessionLocal, QuestionBank

from rag_router import rag_router

# Set up basic logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def ask_next_question(chat_id: int, user_id: int, context: ContextTypes.DEFAULT_TYPE, retry_count: int = 0):
    """Fetches a generated question and sends it to the user with retry logic."""
    user = await get_or_create_user(user_id)
    
    # Check if they exhausted the curriculum
    if user.current_topic_index >= len(AWS_DOMAINS):
        await context.bot.send_message(
            chat_id=chat_id,
            text="🎉 Congratulations! You have mastered all the AWS Cloud Practitioner domains in our curriculum."
        )
        return
    
    current_domain = AWS_DOMAINS[user.current_topic_index]
    
    processing_msg = await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🧠 Generating a question for *{current_domain}*...", 
        parse_mode="Markdown"
    )

    try:
        # 1. Try to fetch from QuestionBank first to avoid hit limits
        async with AsyncSessionLocal() as session:
            stmt = select(QuestionBank).where(
                QuestionBank.domain == current_domain,
                QuestionBank.is_used == 0
            ).limit(1)
            result = await session.execute(stmt)
            bank_q = result.scalar_one_or_none()
            
            if bank_q:
                question_data = json.loads(bank_q.question_data)
                bank_q.is_used = 1
                await session.merge(bank_q)
                await session.commit()
                logger.info(f"Bot: Pulled question from bank for {current_domain}.")
            else:
                logger.warning(f"Bot: QuestionBank empty for {current_domain}. Falling back to real-time generation.")
                question_data = await rag_router.generate_question(current_domain)

        explanation = question_data.get("explanation", "No explanation provided.")
        
        # Send Poll (Explicitly NON-ANONYMOUS)
        poll_message = await context.bot.send_poll(
            chat_id=chat_id,
            question=question_data["question"],
            options=question_data["options"],
            type="quiz",
            correct_option_id=question_data["correct_index"],
            is_anonymous=False
        )

        
        # Track the active poll globally
        context.bot_data[poll_message.poll.id] = {
            "explanation": explanation,
            "user_id": user_id,
            "chat_id": chat_id,
            "correct_option_id": question_data["correct_index"]
        }
        
        # Track user's active poll to prevent /start spam (avoids context.user_data crashes)
        if "user_active_polls" not in context.bot_data:
            context.bot_data["user_active_polls"] = {}
        context.bot_data["user_active_polls"][user_id] = poll_message.poll.id
        
        await context.bot.delete_message(chat_id=chat_id, message_id=processing_msg.message_id)
        
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
            await asyncio.sleep(3)
            await context.bot.delete_message(chat_id=chat_id, message_id=processing_msg.message_id)
            return await ask_next_question(chat_id, user_id, context, retry_count=retry_count + 1)
        else:
            await context.bot.edit_message_text(
                chat_id=chat_id, 
                message_id=processing_msg.message_id, 
                text="⚠️ Sorry, there was an issue generating the question after retries. Please type /start to try again."
            )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command idempotently."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    user_prog = await get_or_create_user(user.id)
    
    # Check if there is already an active question globally
    active_poll_id = context.bot_data.get("user_active_polls", {}).get(user.id)
    if active_poll_id and active_poll_id in context.bot_data:
        await context.bot.send_message(
            chat_id=chat_id,
            text="👋 You already have an active question waiting for you! Please answer it before we move on. 📚"
        )
        return

    welcome_text = (
        f"Welcome back, {user.first_name}! ☁️\n\nReady to continue your AWS Cloud Practitioner journey?"
        if user_prog.questions_asked > 0 else
        "Welcome to the Adaptive AWS Cloud Practitioner Tutor! ☁️\n\n"
        "I will guide you through the official AWS domains using adaptive questioning.\n"
        f"If you answer {STREAK_TARGET} correctly in a row, you advance.\n"
        f"If you miss {WRONG_TARGET} in a row, I'll provide a simplified summary of the topic to help you out.\n\n"
        "Let's get started!"
    )
    
    await context.bot.send_message(chat_id=chat_id, text=welcome_text)
    await ask_next_question(chat_id, user.id, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays help information about the bot."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "📚 **AWS Tutor Help**\n\n"
            "Here is how I help you learn:\n"
            "• **Choose Topics**: Use /menu to select a specific AWS domain.\n"
            "• **Adaptive Learning**: I track your streaks. Answer 3 correctly to level up.\n"
            "• **Manual Flow**: After answering, YOU decide when to see the next question.\n\n"
            "**Commands:**\n"
            "/start - Begin or resume your learning session\n"
            "/menu  - Open the domain selection menu\n"
            "/next  - Manually skip to the next AWS domain\n"
            "/help  - Show this help message"
        ),
        parse_mode="Markdown"
    )

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays the interactive domain selection menu."""
    keyboard = []
    for i, domain in enumerate(AWS_DOMAINS):
        keyboard.append([InlineKeyboardButton(domain, callback_data=f"domain_{i}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message_text = "📋 **Main Menu**\nSelect an AWS Domain to focus on:"
    
    if update.message:
        await update.message.reply_text(message_text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        # Fallback for callback queries
        await update.effective_chat.send_message(message_text, reply_markup=reply_markup, parse_mode="Markdown")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles all inline button clicks."""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    if query.data.startswith("domain_"):
        domain_index = int(query.data.split("_")[1])
        user = await get_or_create_user(user_id)
        
        # Update progression
        user.current_topic_index = domain_index
        user.current_correct_streak = 0
        user.current_wrong_streak = 0
        await save_user(user)
        
        domain_name = AWS_DOMAINS[domain_index]
        await query.edit_message_text(
            text=f"🎯 **Topic Selected:** {domain_name}\nGenerating your first question...",
            parse_mode="Markdown"
        )
        
        # Clear any existing locks
        if "user_active_polls" in context.bot_data and user_id in context.bot_data["user_active_polls"]:
            del context.bot_data["user_active_polls"][user_id]
            
        await ask_next_question(chat_id, user_id, context)

    elif query.data == "next_q":
        await ask_next_question(chat_id, user_id, context)
        
    elif query.data == "show_menu":
        await menu_command(update, context)


async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles incoming poll answers with heavy logging and manual result continuation."""
    answer = update.poll_answer
    poll_id = answer.poll_id
    user_id = answer.user.id
    
    logger.info(f"POLL TRIGGERED: User {user_id} answered Poll {poll_id}")
    
    stored_data = context.bot_data.get(poll_id)
    if not stored_data:
        logger.warning(f"POLL MISSING: Poll {poll_id} not found in bot_data")
        return
        
    chat_id = stored_data.get("chat_id", user_id) 
    explanation = stored_data.get("explanation", "No explanation available.")
    correct_option_id = stored_data["correct_option_id"]
    
    # Cleanup memory
    del context.bot_data[poll_id]
    if "user_active_polls" in context.bot_data and user_id in context.bot_data["user_active_polls"]:
        del context.bot_data["user_active_polls"][user_id]

    selected_option = answer.option_ids[0]
    is_correct = (selected_option == correct_option_id)
    
    user = await get_or_create_user(user_id)
    
    result_prefix = "✅ **Correct!**" if is_correct else "❌ **Incorrect.**"
    
    # Buttons for next steps
    keyboard = [
        [
            InlineKeyboardButton("⏭️ Next Question", callback_data="next_q"),
            InlineKeyboardButton("📋 Menu", callback_data="show_menu")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send Explanation with Choices (with Markdown fallback)
    explanation_text = f"{result_prefix}\n\n💡 **Explanation:**\n{explanation}"
    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=explanation_text,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    except telegram.error.BadRequest as e:
        if "Can't parse entities" in str(e):
            logger.warning(f"Markdown parsing failed for explanation. Falling back to plain text. Error: {e}")
            # Simplified text without markdown markers
            plain_prefix = "✅ Correct!" if is_correct else "❌ Incorrect."
            plain_text = f"{plain_prefix}\n\nExplanation:\n{explanation}"
            await context.bot.send_message(
                chat_id=chat_id,
                text=plain_text,
                reply_markup=reply_markup
            )
        else:
            raise


    # Process Streaks (Silent update, no auto-next)
    if is_correct:
        user.correct_answers += 1
        user.current_correct_streak += 1
        user.current_wrong_streak = 0
        
        if user.current_correct_streak >= STREAK_TARGET:
            user.current_topic_index += 1
            user.current_correct_streak = 0
            await context.bot.send_message(
                chat_id=chat_id,
                text="🌟 **Level Up!** 🌟\nYou've mastered this domain! Use the buttons above or /menu to continue."
            )
            
    else:
        user.current_wrong_streak += 1
        user.current_correct_streak = 0
        
        if user.current_wrong_streak >= WRONG_TARGET:
            current_domain = AWS_DOMAINS[user.current_topic_index] if user.current_topic_index < len(AWS_DOMAINS) else "Unknown"
            user.current_wrong_streak = 0 
            
            await context.bot.send_message(
                chat_id=chat_id,
                text="It looks like you're struggling a bit. Reach out for the summary in the menu or continue practicing."
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


async def next_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manually advances the user to the next AWS domain."""
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    user = await get_or_create_user(user_id)
    
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
    
    # Clear any active poll locks
    if "user_active_polls" in context.bot_data and user_id in context.bot_data["user_active_polls"]:
        del context.bot_data["user_active_polls"][user_id]
        
    await ask_next_question(chat_id, user_id, context)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Exception while handling an update:", exc_info=context.error)
    if isinstance(update, Update) and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ An internal error occurred. Please try again later."
        )

async def post_init(application) -> None:
    await init_db()
    logger.info("Database initialization complete.")

if __name__ == '__main__':
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    
    if "bot_data" not in application.bot_data:
        application.bot_data = {}

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('next', next_topic))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('menu', menu_command))
    application.add_handler(PollAnswerHandler(receive_poll_answer))
    application.add_handler(CallbackQueryHandler(handle_callback))
    application.add_error_handler(error_handler)
    
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=["message", "poll_answer", "poll", "callback_query"])