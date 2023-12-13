from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from config.config import bot_config
from db.model import Base

engine = create_async_engine(url=bot_config.db_url,
                             echo=True)

async_session = async_sessionmaker(engine)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
