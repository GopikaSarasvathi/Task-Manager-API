from sqlalchemy.orm import Session
from app.models import User
from app.models import Task
from app.schema import UserResponse
from app.schema import TaskUpdate
from app.schema import TaskRequest
from app.utils.dependencies import get_password_hash

def create_user(db: Session, user: UserResponse):
    hashed_pw = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_task(db:Session, task:TaskRequest, user_id: int):
    db_task=Task(title=task.title, completed=task.completed, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db:Session, task:TaskUpdate, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return {"message": "Task not found"}
    if task.completed==None:
        db_task.title=task.title     
    elif task.title==None:
       db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task
