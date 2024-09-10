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
    streak = Column(Integer, default=0)
    top_group = Column(Integer, default=0)
    top_percent = Column(Integer, default=0)
    telegram_id = Column(Integer, unique=True, index=True)
    attempts_left = Column(Integer, default=5)
    wallet = Column(Integer, default=0)
    
    completed_tasks = relationship('UserTaskCompletion', back_populates='user')
    friends = relationship("Fren", back_populates="user")
    rewards = relationship("Reward", back_populates="user")

class Fren(Base):
    __tablename__ = "frens"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    fren_telegram_id = Column(Integer, index=True)

    user = relationship("User", back_populates="friends")

class Reward(Base):
    __tablename__ = "rewards"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    age = Column(Integer, default=0)
    boost = Column(Integer, default=0)
    game = Column(Float, default=0.0)
    daily = Column(Float, default=0.0)
    frens = Column(Float, default=0.0)
    premium = Column(Integer, default=0)
    tasks = Column(Integer, default=0)
    total = Column(Float, default=0.0)

    user = relationship("User", back_populates="rewards")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    ton = Column(Float, nullable=True)
    url = Column(String, nullable=True)
    reward = Column(String, nullable=False)

class UserTaskCompletion(Base):
    __tablename__ = 'user_task_completions'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True)

    user = relationship('User', back_populates='completed_tasks')
    task = relationship('Task')
