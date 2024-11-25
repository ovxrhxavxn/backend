from pydantic import BaseModel

from database.annotated_types import intpk, utcnow
from .enums import Consumable


class Note(BaseModel):

    id: intpk
    date: utcnow
    consumable: Consumable
    count: int
