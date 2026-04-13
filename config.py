import os
from dotenv import load_dotenv

# Load explicitly or allow docker environment to provide these variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///fallback.db")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://sakhi_engine:11434")

ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")


# Hardcoded AWS Cloud Practitioner Curriculum Domains
AWS_DOMAINS = [
    "Domain 1: Cloud Concepts",
    "Domain 2: Security and Compliance",
    "Domain 3: Cloud Technology and Services",
    "Domain 4: Billing, Pricing, and Support"
]

STREAK_TARGET = 3  # Hits needed to level up
WRONG_TARGET = 3 # Fails needed to get custom summary
