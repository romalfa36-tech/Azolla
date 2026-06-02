from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import Settings

settings = Settings()

engine = create_async_engine(settings.database_url, echo=True)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db():
    from models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
