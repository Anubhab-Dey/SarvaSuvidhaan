# This file manages the DB Connectivity and gives you a session object when `get_db` is called.

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Atomic DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        async with session.begin():  # ← Transaction starts here
            yield session  # ← Everything in your route runs inside this
