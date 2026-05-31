from fastapi import FastAPI
from app.db.database import Base, engine

from app.models.user import User
from app.models.tenant import Tenant
from app.models.tenant_user import TenantUser

app = FastAPI()

# create tables (sementara untuk dev)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "AI Agent API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}