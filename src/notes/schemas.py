from datetime import date

from pydantic import BaseModel

from .enums import Consumable


class NoteBase(BaseModel):

    date: date
    consumable: Consumable
    count: int


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):

    id: int

    class Config:
        from_attributes = True