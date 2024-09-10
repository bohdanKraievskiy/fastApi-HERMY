from sqlalchemy.orm import Session
from ..models.user import User
from datetime import datetime
def create_user(db: Session, username: str, telegram_id: int,age: int,top_group: int,top_percent:int,is_premium:bool,streak:int):
    new_user = User(username=username,telegram_id=telegram_id, age=age,top_group=top_group,top_percent=top_percent,is_premium=is_premium,last_seen=datetime.now,last_reward_date=datetime.now,streak=streak)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
