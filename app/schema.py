from typing import Optional
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    username: str
    email:EmailStr
    password: str

    model_config = {
        "from_attributes": True
    }
    
class TaskRequest(BaseModel): 
    title: str
    completed:bool

    model_config = {
        "from_attributes": True
    }

class TaskUpdate(BaseModel): 
    title: Optional[str] = None
    completed:Optional[bool] = None
 
class LoginSchema(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
