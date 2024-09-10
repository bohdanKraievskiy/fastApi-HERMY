from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.services.user_service import create_user, get_user_by_id
from server.database import get_db

router = APIRouter()

@router.post("/")
def create_new_user(username: str, telegram_id: int, age: int, top_group: int, top_percent: int, is_premium: bool, streak: int, db: Session = Depends(get_db)):
    new_user = create_user(db, username, telegram_id, age, top_group, top_percent, is_premium, streak)
    return new_user

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        return {"message": "User not found"}
    return user
