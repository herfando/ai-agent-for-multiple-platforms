from pydantic import BaseModel

class IncomingMessage(BaseModel):
    conversation_id: str
    content: str
    role: str = "user"