from datetime import date

from database.repositories import AbstractNoteRepository
from .schemas import NoteCreate, Note
from .enums import Consumable


class NoteService:

    def __init__(self, repo: type[AbstractNoteRepository]):
        self._repo = repo()


    async def get_by_id(self, id: int):
        return await self._repo.get_by_id(id)

    
    async def get_by_year(self, year: int) -> list[Note]:
        rows = await self._repo.get_by_year(year)
        return [Note.model_validate(row[0]) for row in rows]
        

    async def add(self, schema: NoteCreate):
        await self._repo.add(schema.model_dump())


    async def delete(self, id: int):
        await self._repo.delete(id)


    async def edit_date(self, id: int, new_date: date):
        await self._repo.edit_date(id, new_date)


    async def edit_count(self, id: int, new_count: int):
        await self._repo.edit_count(id, new_count)
    

    async def edit_consumable(self, id: int, new_comsumable: Consumable):
        await self._repo.edit_consumable(id, new_comsumable)


    async def get(self, limit: int, offset: int) -> list[Note]:
        rows = await self._repo.get(limit, offset)
        return [Note.model_validate(row[0]) for row in rows]