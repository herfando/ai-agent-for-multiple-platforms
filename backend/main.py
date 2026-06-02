from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.messages import router as message_router
from app.api.conversations import (
    router as conversation_router
)



app = FastAPI()

# ROUTES
app.include_router(auth_router, prefix="/auth")

app.include_router(
    message_router,
    prefix="/messages",
    tags=["Messages"]
)
app.include_router(
    conversation_router,
    prefix="/conversations",
    tags=["Conversations"]
)

# ROOT
@app.get("/")
def root():
    return {"message": "AI Agent API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

    