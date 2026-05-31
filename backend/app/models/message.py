from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime
from app.models.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True)

    conversation_id = Column(String, index=True)

    role = Column(String)  # user / ai / system
    content = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)