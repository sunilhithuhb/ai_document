from fastapi import FastAPI

from app.database import engine, Base
from app.models import User, Document
from app.routers.users import router as user_router
from app.routers.document import router as document_router

Base.metadata.create_all(bind=engine)

app =FastAPI(
    
    title="Document Intelligence API",
    description="API for document upload, search and question answering",
    version="1.0.0"
)
app.include_router(user_router)
app.include_router(document_router)

@app.get("/")
def home():
    return {'message':'api document intelligence Api is doing'}