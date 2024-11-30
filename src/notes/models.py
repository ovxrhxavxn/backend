from sqlalchemy.orm import Mapped, mapped_column

from database.stuff import Base
from database.annotated_types import intpk, utcnow
from .enums import Consumable


class Note(Base):

    __tablename__ = 'notes'

    id: Mapped[intpk]
    date: Mapped[utcnow]
    consumable: Mapped[Consumable] = mapped_column()
    count: Mapped[int] = mapped_column()