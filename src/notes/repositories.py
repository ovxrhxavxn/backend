from datetime import date

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


    async def edit_date(self, id: int, new_date: date):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == id).values(date = new_date)

            await session.execute(stmt)
            await session.commit()

        
    async def edit_count(self, id: int, new_count: int):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == id).values(count = new_count)

            await session.execute(stmt)
            await session.commit()


    async def edit_consumable(self, id: int, new_consumable: int):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == id).values(consumable = new_consumable)

            await session.execute(stmt)
            await session.commit()


    async def get(self, limit: int, offset: int):
        async with async_session_maker() as session:
            query = select(self.model).limit(limit).offset(offset)

            result = await session.execute(query)

            return result.all()