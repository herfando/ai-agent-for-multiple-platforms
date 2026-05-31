from sqlalchemy import Column, String
from app.models.base import Base

class Channel(Base):
    __tablename__ = "channels"

    id = Column(String, primary_key=True)
    name = Column(String)  # instagram, whatsapp, telegram