from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

import api.const as const

ASYNC_DB_URL = f"mysql+aiomysql://{const.USER}:{const.PASSWORD}@{const.HOST}:{const.PORT}/{const.DB}?charset=utf8mb4"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_db_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession)

Base = declarative_base()


async def get_db():
    async with async_db_session() as db:
        yield db
