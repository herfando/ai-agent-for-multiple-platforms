from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db

from app.schemas.message import IncomingMessage
from app.services.message_service import save_message
from app.services.conversation_state_service import (
    get_or_create_state
)

router = APIRouter()

@router.post("/")
def create_message(
    payload: IncomingMessage,
    db: Session = Depends(get_db)
):
    state = get_or_create_state(
        db,
        payload.conversation_id
    )
    return save_message(
        db,
        payload.conversation_id,
        payload.content,
        payload.role
    )