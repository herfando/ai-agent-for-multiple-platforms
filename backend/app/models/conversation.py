from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.models.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    contact_id = Column(String, index=True)
    channel_account_id = Column(String, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)