# This file contains miscellaneous DB Utilities


from app.database import engine
from app.models.wheel_specification_form import Base


async def create_all_tables():
    """
    Automatically creates all tables on app startup if they don't exist.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created on startup.")
