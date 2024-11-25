from contextlib import asynccontextmanager

from fastapi import (

    FastAPI
)


@asynccontextmanager
async def lifespan(app: FastAPI):

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