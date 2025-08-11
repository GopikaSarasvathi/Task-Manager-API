from fastapi import Depends, FastAPI
from app.tasks.routes import router as tasks_router
from app.database import engine, Base
from app.models import User 
from app.models import Task
from app.utils.auth import get_current_user
from app.auth import router as auth_router


Base.metadata.create_all(bind=engine)
 

app = FastAPI()

app.include_router(tasks_router)
app.include_router(auth_router)

