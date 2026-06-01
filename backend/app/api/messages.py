from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db

from app.schemas.message import IncomingMessage
from app.services.message_service import save_message

router = APIRouter()

@router.post("/")
def create_message(
    payload: IncomingMessage,
    db: Session = Depends(get_db)
):
    return save_message(
        db,
        payload.conversation_id,
        payload.content,
        payload.role
    )