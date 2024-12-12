from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
    

class Base(DeclarativeBase): pass


db_url = "sqlite+aiosqlite:///src/database/app.db"

async_engine = create_async_engine(
             
            url=db_url, connect_args={"check_same_thread": False}
        )
        
async_session_maker: type[AsyncSession] = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session():

    async with async_session_maker() as session:

        yield session

        
async def create_tables():
        
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)