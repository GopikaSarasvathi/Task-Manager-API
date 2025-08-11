from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import UserResponse
from app.schema import TaskRequest
from app.schema import TaskUpdate
from app.crud import create_user
from app.crud import create_task
from app.crud import update_task
from app.models import User
from app.models import Task
from app.utils.auth import get_current_user
from fastapi_cache.decorator import cache
 


router = APIRouter()

@router.post("/signup")
def signup(user: UserResponse, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)


@router.post("/addTask")
def addTask(task:TaskRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    existing_user = db.query(User).filter(User.id == user.id).first()
    if existing_user:
        return create_task(db, task, user.id)
    else:
        return {"message": "User not found or not logged in"}
    
@router.patch("/updateTask/{task_id}")
def updateTask(task_id: int, task:TaskUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    
    if db_task:
        return update_task(db, task, task_id)
    else:
            return {"message":"Task doesn't belong to user"}       


@router.get("/getTasks")
def get_tasks(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    
    existing_user = db.query(User).filter(User.id == user.id).first()
    if existing_user:
        tasks = db.query(Task).filter(Task.user_id == user.id).all()
        return tasks
    else:
        return {"message": "User not found or not logged in"}
    
@router.delete("/removeTask/{task_id}")
def updateTask(task_id:int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return {"message":"Task removed"}
    else:
        return {"message":"Task doesn't belong to user or Task not found"}  
    
@router.get("/completedTasks")
def updateTask(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.user_id == user.id,Task.completed==True).all()
    if db_task:
        return db_task
    else:
        return {"message":"Task doesn't belong to user or Task not found"}  