from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    avatar = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    is_premium = Column(Boolean, default=False)
    last_seen = Column(DateTime)
    last_reward_date = Column(DateTime)
    streak = Column(Integer,default=0)
    top_group = Column(Integer, default=0)
    top_percent = Column(Integer, default=0)
    telegram_id = Column(Integer, unique=True, index=True)
    attempts_left = Column(Integer, default=5)
    wallet = Column(Integer, default=0)
    
    completed_tasks = relationship('UserTaskCompletion', back_populates='user')
    friends = relationship("Friend", back_populates="user")
    tasks = relationship("UserTask", back_populates="user")