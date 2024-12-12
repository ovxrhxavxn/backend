from typing import Annotated
from datetime import date

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from dependencies import get_pagination_params
from notes.services import NoteService
from notes.dependencies import get_note_service
from notes.enums import Consumable


templates = Jinja2Templates(directory='src/templates')

router = APIRouter(

    prefix='/templates',
    tags=['Templates']
)


@router.get('/add_button', response_class=HTMLResponse)
async def get_add_button(


    request: Request,

    ):
    
    return templates.TemplateResponse('add_button.html', {'request' : request})


@router.get('/main_content', response_class=HTMLResponse)
async def get_main_content(


    request: Request,

    ):
    
    return templates.TemplateResponse('main_content.html', {'request' : request})


@router.get('/notes/pagination', response_class=HTMLResponse)
async def get_notes(


    request: Request,
    service: Annotated[NoteService, Depends(get_note_service)],
    pagination: Annotated[dict, Depends(get_pagination_params)]

    ):
    
    notes = await service.get(pagination['limit'], pagination['offset'])

    consumables = [consumable for consumable in Consumable]

    return templates.TemplateResponse('notes.html', {'request' : request, 'notes' : notes, 'consumables': consumables})


@router.get('/notes', response_class=HTMLResponse)
async def get_all_notes(


    request: Request,
    service: Annotated[NoteService, Depends(get_note_service)],

    ):
    
    notes = await service.get_all()

    consumables = [consumable for consumable in Consumable]

    return templates.TemplateResponse('notes.html', {'request' : request, 'notes' : notes, 'consumables': consumables})


@router.get('/add_note', response_class=HTMLResponse)
async def get_add_note_page(request: Request,):

    consumables = [consumable for consumable in Consumable]

    today = date.today()

    return templates.TemplateResponse('add_note.html', {'request': request, 'consumables': consumables, 'date': today})


@router.get('/notes/{year}', response_class=HTMLResponse)
async def get_notes_by_year(
    
    request: Request,
    year: int,
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    notes = await service.get_by_year(year)

    return templates.TemplateResponse('notes.html', {'request': request, 'notes': notes})