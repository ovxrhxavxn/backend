from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from notes.router import router as notes_router
from templates.router import router as templates_router
from database.stuff import create_tables
from templates.router import templates


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

    yield


app = FastAPI(

    lifespan=lifespan,
    title='DiaLog',
    summary='Backend для приложения DiaLog'

    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


routers = [

    notes_router,
    templates_router
]

for router in routers:
    app.include_router(router)