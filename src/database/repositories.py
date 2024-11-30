from abc import ABC, abstractmethod
from datetime import date

from notes.schemas import Note
from notes.enums import Consumable


class SQLAlchemyRepository(ABC):

    model = None


class AbstractNoteRepository(ABC):

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
    async def edit_date(self, id: int, new_date: date):
        raise NotImplementedError
    
    @abstractmethod
    async def edit_count(self, id: int, new_count: int):
        raise NotImplementedError
    
    @abstractmethod
    async def edit_consumable(self, id: int, new_consumable: Consumable):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self, limit: int, offset: int):
        raise NotImplementedError