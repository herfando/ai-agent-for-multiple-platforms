import uuid

from app.models.message import Message

def save_message(db, conversation_id, content, role):

    message = Message(
        id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        content=content,
        role=role
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message