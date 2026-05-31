from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.models.base import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    name = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)