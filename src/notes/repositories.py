from sqlalchemy import (

    select, 
    delete, 
    insert, 
    update,
    func
)

from .models import Note
from database.stuff import async_session_maker
from database.repositories import AbstractNoteRepository, SQLAlchemyRepository


class NoteRepository(AbstractNoteRepository, SQLAlchemyRepository):

    model = Note

    async def get_rows_count(self):
        async with async_session_maker() as session:
            query = select(self.model)

            result = await session.execute(query)

            return result
        
        
    async def get_by_id(self, id: int) -> Note:
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id == id)

            result = await session.execute(query)

            return result.scalar_one()


    async def get_by_year(self, year: int):
        async with async_session_maker() as session:
            query = select(self.model).where(func.extract('year', self.model.date) == year)

            result = await session.execute(query)

            return result.all()
        

    async def add(self, schema: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**schema)

            await session.execute(stmt)
            await session.commit()

        
    async def delete(self, id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == id)

            await session.execute(stmt)
            await session.commit()

    
    async def update_note(self, id: int, schema: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == id).values(**schema)

            await session.execute(stmt)
            await session.commit()


    async def get(self, limit: int, offset: int):
        async with async_session_maker() as session:
            query = select(self.model).limit(limit).offset(offset)

            result = await session.execute(query)

            return result.all()
        
        
    async def get_all(self):
        async with async_session_maker() as session:
            query = select(self.model)

            result = await session.execute(query)

            return result.all()