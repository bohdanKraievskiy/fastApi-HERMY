from sqlalchemy.orm import Session
from ..models.task import Task, UserTaskCompletion

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_tasks_for_user(db: Session, user_id: int):
    tasks = db.query(
        Task,
        UserTaskCompletion.completion_date
    ).outerjoin(
        UserTaskCompletion,
        (Task.id == UserTaskCompletion.task_id) & (UserTaskCompletion.user_id == user_id)
    ).all()

    result = []
    for task, completion_date in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "ton": task.ton,
            "url": task.url,
            "reward": task.reward,
            "completed": completion_date is not None
        })
    return result

def complete_task(db: Session, user_id: int, task_id: int):
    completion = UserTaskCompletion(user_id=user_id, task_id=task_id)
    db.add(completion)
    db.commit()
    return {"message": "Task marked as completed"}
