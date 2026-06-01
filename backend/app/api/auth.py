from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.auth.service import register_user, login_user

router = APIRouter()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    return register_user(db, email, password)


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    token = login_user(db, email, password)

    if not token:
        return {"error": "Invalid credentials"}

    return {"access_token": token}