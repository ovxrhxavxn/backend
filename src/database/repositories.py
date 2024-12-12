from abc import ABC, abstractmethod
from datetime import date

from notes.schemas import Note


class SQLAlchemyRepository(ABC):

    model = None


class AbstractNoteRepository(ABC):

    @abstractmethod
    async def get_rows_count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_by_year(self, date: date):
        raise NotImplementedError
    
    @abstractmethod
    async def add(self, schema: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def delete(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Note:
        raise NotImplementedError
    
    @abstractmethod
    async def update_note(self, id: int, schema: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self, limit: int, offset: int):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError