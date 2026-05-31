from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.models.base import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(String, primary_key=True)
    name = Column(String)
class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(String, primary_key=True)

    tenant_id = Column(String)
    plan_id = Column(String)

    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)