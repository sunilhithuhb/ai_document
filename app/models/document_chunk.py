from sqlalchemy import Column,Integer,Text,ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class DocumentChunk(Base):
    __tablename__= "documwent_chunk"

    pd = Column(Integer,primary_key=True,index=True)
    document_id=Column(Integer,ForeignKey("documents.id"),nullable=False)
    chunk_text=Column(Text,nullable=False)
    chunk_index=Column(Integer,nullable=False)

    