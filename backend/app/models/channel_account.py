from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.models.base import Base

class ChannelAccount(Base):
    __tablename__ = "channel_accounts"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    channel_id = Column(String, index=True)

    account_identifier = Column(String)  # IG username / WA number
    access_token = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)