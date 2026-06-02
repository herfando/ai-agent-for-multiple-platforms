import uuid

from app.models.conversation_state import ConversationState


def get_or_create_state(db, conversation_id):

    state = (
        db.query(ConversationState)
        .filter(
            ConversationState.conversation_id == conversation_id
        )
        .first()
    )

    if state:
        return state

    state = ConversationState(
        id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        intent="unknown",
        stage="lead",
        summary="",
        last_action=""
    )

    db.add(state)
    db.commit()
    db.refresh(state)

    return state