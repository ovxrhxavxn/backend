from typing import Annotated

from fastapi import (
    
    APIRouter, 
    Depends
)

from .services import NoteService
from .schemas import NoteCreate, NoteBase
from .dependencies import get_note_service


router = APIRouter(

    prefix='/notes',
    tags=['Notes']
)


@router.post('/')
async def add_note(

    note: NoteCreate,
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.add(note)


@router.delete('/{id}')
async def delete_note(

    id: int, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.delete(id)


@router.put('/{id}')
async def update_note(
    
    id: int, 
    note: NoteBase, 
    service: Annotated[NoteService, Depends(get_note_service)]
    
    ):

    await service.update_note(id, note)