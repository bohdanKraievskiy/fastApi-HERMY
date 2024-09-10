from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy import Column, Integer, String, Float

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