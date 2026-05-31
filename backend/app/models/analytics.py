from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from app.models.base import Base

class AnalyticsDaily(Base):
    __tablename__ = "analytics_daily"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    date = Column(DateTime)

    messages_count = Column(Integer)
    leads_count = Column(Integer)