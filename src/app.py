from contextlib import asynccontextmanager

from fastapi import (

    FastAPI
)

from notes.router import router as notes_router
from database.stuff import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

    yield


app = FastAPI(

    lifespan=lifespan,
    title='DiaLog',
    summary='Backend для приложения DiaLog'

    )

routers = [

    #TODO: добавить роутеры
]

for router in routers:
    app.include_router(router)