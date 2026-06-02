import uuid

from app.models.message import Message
from app.services.queue_service import push_ai_job

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

    # Push the message to the AI job queue
    push_ai_job({
    "conversation_id": conversation_id,
    "message_id": message.id,
    "content": content
})

    return message