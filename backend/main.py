from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.messages import router as message_router
from app.api.conversations import (
    router as conversation_router
)
from app.api.webhooks.instagram import router as ig_router
from app.api.webhooks.whatsapp import router as wa_router
from app.api.meta import router as meta_router


app = FastAPI()

# ROUTES
app.include_router(auth_router, prefix="/auth")
app.include_router(meta_router, prefix="/meta", tags=["Meta OAuth"])

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

# WEBHOOKS
app.include_router(ig_router, prefix="/webhooks")
app.include_router(wa_router, prefix="/webhooks")

# ROOT
@app.get("/")
def root():
    return {"message": "AI Agent API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

    