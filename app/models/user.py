from sqlalchemy import Column,String,Integer 
from sqlalchemy.orm import relationship 

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username=Column(String(100),unique=True,nullable=False)
    email=Column(String(255),unique=True,nullable=True)
    password=Column(String(255),unique=True,nullable=True)

    documents = relationship("Document",back_populates="user")
    