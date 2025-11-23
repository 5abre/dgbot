from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dgbot.core.config import config
from dgbot.backend.models import *  

engine = create_async_engine(url=config.db_url)

async_session = async_sessionmaker(engine)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)