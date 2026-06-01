from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
import uuid

def register_user(db: Session, email: str, password: str):

    user = User(
        id=str(uuid.uuid4()),
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({
        "user_id": user.id,
        "email": user.email
    })

    return token