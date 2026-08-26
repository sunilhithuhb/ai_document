from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship 

from app.database import Base
 
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer,primary_key=True,index=True)
    filename=Column(String(255),nullable=False)
    file_path=Column(String(500),nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship("User",back_populates='documents')