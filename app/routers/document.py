from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import os
import shutil

from app.database import get_db
from app.models.document import Document
from app.models.user import User
from app.schemas.documents import DocumentResponse


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload", response_model=DocumentResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db) 
):
    # 1. Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # 2. Create uploads directory
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    # 3. Create file path
    file_path = os.path.join(upload_dir, file.filename)

    # 4. Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 5. Create document record
    document = Document(
        filename=file.filename,
        file_path=file_path,
        user_id=1
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document