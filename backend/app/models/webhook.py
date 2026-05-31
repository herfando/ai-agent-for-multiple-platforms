from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.models.base import Base

class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id = Column(String, primary_key=True)

    source = Column(String)
    payload = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)