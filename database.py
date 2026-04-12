import logging
from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from config import DATABASE_URL

logger = logging.getLogger(__name__)

Base = declarative_base()

class UserProgress(Base):
    __tablename__ = 'user_progress'
    
    user_id = Column(BigInteger, primary_key=True)
    current_topic_index = Column(Integer, default=0)
    questions_asked = Column(Integer, default=0)
    correct_answers = Column(Integer, default=0)
    current_correct_streak = Column(Integer, default=0)
    current_wrong_streak = Column(Integer, default=0)

class QuestionBank(Base):
    __tablename__ = 'question_bank'
    
    id = Column(Integer, primary_key=True)
    domain = Column(String)
    question_data = Column(String) # JSON string
    is_used = Column(Integer, default=0) # 0 = fresh, 1 = used



# Create an async database engine matching the injected DATABASE_URL
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized with tables.")

async def get_or_create_user(user_id: int):
    async with AsyncSessionLocal() as session:
        user = await session.get(UserProgress, user_id)
        if not user:
            user = UserProgress(user_id=user_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

async def save_user(user: UserProgress):
    async with AsyncSessionLocal() as session:
        session.add(user)
        await session.merge(user)
        await session.commit()
