from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.db.database import Base

class TenantUser(Base):
    __tablename__ = "tenant_users"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    user_id = Column(String, index=True)

    role = Column(String)  # admin / staff

    created_at = Column(DateTime, default=datetime.utcnow)