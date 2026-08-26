from fastapi import FastAPI

from app.database import engine, Base
from app.models import User, Document


Base.metadata.create_all(bind=engine)

app =FastAPI(
    
    title="Document Intelligence API",
    description="API for document upload, search and question answering",
    version="1.0.0"
)

@app.get("/")
def home():
    return {'message':'api document intelligence Api is doing'}