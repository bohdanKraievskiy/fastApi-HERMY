from sqlalchemy.orm import Session
from datetime import datetime
from ..models.user import User, Fren, Reward

def create_user(db: Session, username: str, telegram_id: int, age: int, top_group: int, top_percent: int, is_premium: bool, streak: int):
    new_user = User(
        username=username,
        telegram_id=telegram_id,
        age=age,
        top_group=top_group,
        top_percent=top_percent,
        is_premium=is_premium,
        last_seen=datetime.now,  # Call datetime.now() to get the current datetime
        last_reward_date=datetime.now,
        streak=streak
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Add initial entries for friends and rewards
    # This assumes that Fren and Reward are optional or have default values
    db.add(Fren(user_id=new_user.id, fren_telegram_id=None))
    db.add(Reward(user_id=new_user.id))
    db.commit()

    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
