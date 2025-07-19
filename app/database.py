# This file manages the DB Connectivity and gives you a session object when `get_db` is called.

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Create engine with max pool size from .env
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=settings.DB_CONNLMT,
    max_overflow=0,
)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            yield session
