from database.repositories import AbstractNoteRepository
from .schemas import NoteCreate, NoteBase, Note


class NoteService:

    def __init__(self, repo: type[AbstractNoteRepository]):
        self._repo = repo()

    
    async def get_rows_count(self) -> int:
        rows = await self._repo.get_rows_count()

        return len([Note.model_validate(row[0]) for row in rows])


    async def get_by_id(self, id: int):
        return await self._repo.get_by_id(id)

    
    async def get_by_year(self, year: int) -> list[Note]:
        rows = await self._repo.get_by_year(year)
        return [Note.model_validate(row[0]) for row in rows]
        

    async def add(self, schema: NoteCreate):
        await self._repo.add(schema.model_dump())


    async def delete(self, id: int):
        await self._repo.delete(id)


    async def update_note(self, id: int, schema: NoteBase):
        await self._repo.update_note(id, schema.model_dump())


    async def get(self, limit: int, offset: int) -> list[Note]:
        rows = await self._repo.get(limit, offset)
        return [Note.model_validate(row[0]) for row in rows]
    

    async def get_all(self):
        rows = await self._repo.get_all()
        return [Note.model_validate(row[0]) for row in rows]