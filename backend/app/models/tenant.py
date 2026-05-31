from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.db.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)