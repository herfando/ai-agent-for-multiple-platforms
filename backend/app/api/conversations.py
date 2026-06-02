from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.deps import get_db
from app.models.conversation_state import (
    ConversationState
)

router = APIRouter()


@router.get("/{conversation_id}/state")
def get_state(
    conversation_id: str,
    db: Session = Depends(get_db)
):
    return (
        db.query(ConversationState)
        .filter(
            ConversationState.conversation_id
            == conversation_id
        )
        .first()
    )