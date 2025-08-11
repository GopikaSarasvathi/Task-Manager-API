from sqlalchemy import Column,Integer,String,Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Task(Base):
   __tablename__="tasks"
   id = Column(Integer,primary_key=True, index=True)
   title = Column(String, index=True)
   completed = Column(Boolean, default=False)
   user_id = Column(Integer, ForeignKey("users.id"))
   user = relationship("User", back_populates="tasks")


class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="user")