from sqlalchemy import Column, String, Text
from app.models.base import Base

class AIModel(Base):
    __tablename__ = "ai_models"

    id = Column(String, primary_key=True)
    name = Column(String)  # llama / deepseek
class AIPrompt(Base):
    __tablename__ = "ai_prompts"

    id = Column(String, primary_key=True)

    tenant_id = Column(String, index=True)
    content = Column(Text)
class AIMemory(Base):
    __tablename__ = "ai_memory"

    id = Column(String, primary_key=True)

    contact_id = Column(String, index=True)
    memory = Column(Text)