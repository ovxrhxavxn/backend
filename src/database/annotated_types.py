from typing import Annotated
from datetime import date, datetime as dt, UTC

from sqlalchemy.orm import mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
utcnow = Annotated[date, mapped_column(default=dt.now(UTC).date())]