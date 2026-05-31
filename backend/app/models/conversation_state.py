from sqlalchemy import Column, String, Text
from app.models.base import Base

class ConversationState(Base):
    __tablename__ = "conversation_state"

    id = Column(String, primary_key=True)

    conversation_id = Column(String, unique=True)

    intent = Column(String)
    stage = Column(String)  # lead / customer / closing

    summary = Column(Text)
    last_action = Column(Text)