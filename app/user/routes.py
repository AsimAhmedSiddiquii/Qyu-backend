from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.user.models import User
from app.user.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get-users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/new-user")
def create_user(user_data: dict, db: Session = Depends(get_db)):
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user