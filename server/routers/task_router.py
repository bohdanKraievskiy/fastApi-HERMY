from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.services.task_service import get_all_tasks, get_tasks_for_user,complete_task
from server.database import get_db

router = APIRouter()

@router.get("/")
def list_tasks_for_user(user_id: int, db: Session = Depends(get_db)):
    tasks = get_tasks_for_user(db, user_id)
    return tasks

@router.post("/{task_id}/complete")
def mark_task_completed(task_id: int, user_id: int, db: Session = Depends(get_db)):
    return complete_task(db, user_id, task_id)