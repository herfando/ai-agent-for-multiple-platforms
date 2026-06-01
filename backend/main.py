from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI()

# ROUTES
app.include_router(auth_router, prefix="/auth")

# ROOT
@app.get("/")
def root():
    return {"message": "AI Agent API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}