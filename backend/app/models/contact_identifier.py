from sqlalchemy import Column, String
from app.models.base import Base

class ContactIdentifier(Base):
    __tablename__ = "contact_identifiers"

    id = Column(String, primary_key=True)

    contact_id = Column(String, index=True)

    platform = Column(String)  # instagram / whatsapp / telegram
    external_id = Column(String)  # user id / phone number