from typing import Annotated
from datetime import date

from fastapi import APIRouter, Depends, Query

from .services import NoteService
from .schemas import NoteCreate, Note
from .dependencies import get_note_service
from .enums import Consumable


router = APIRouter(

    prefix='/notes',
    tags=['Notes']
)


def get_pagination_params(
        
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0)

    ):

    return {"offset": offset, "limit": limit}


@router.post('/')
async def add_note(

    note: NoteCreate, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.add(note)


@router.delete('/')
async def delete_note(

    id: int, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.delete(id)


@router.patch('/{id}/date')
async def edit_note_date(

    id: int, 
    new_date: date, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.edit_date(id, new_date)


@router.patch('/{id}/consumable')
async def edit_note_consumable(

    id: int, 
    new_consumable: Consumable, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.edit_consumable(id, new_consumable)


@router.patch('/{id}/count')
async def edit_note_count(

    id: int, 
    new_count: int, 
    service: Annotated[NoteService, Depends(get_note_service)]

    ):

    await service.edit_count(id, new_count)


@router.get('/', response_model=list[Note])
async def get_notes(

    service: Annotated[NoteService, Depends(get_note_service)],
    pagination: Annotated[dict, Depends(get_pagination_params)]

    ):
    
    return await service.get(pagination['limit'], pagination['offset'])


@router.get('/{year}')
async def get_notes_by_year(
    
    year: int,
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    return await service.get_by_year(year)