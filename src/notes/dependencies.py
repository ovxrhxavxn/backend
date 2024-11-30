from .services import NoteService
from .repositories import NoteRepository


def get_note_service():
    return NoteService(NoteRepository)