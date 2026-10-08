from app.services.document_proccesors import (
    extract_text_from_pdf,
    split_text_into_chunks,
    save_document_chunks
)

from app.database import SessionLocal


file_path = "uploads/Company_Search.pdf"

text = extract_text_from_pdf(file_path)

chunks = split_text_into_chunks(text)

print("Total chunks:", len(chunks))

db = SessionLocal()

save_document_chunks(
    db=db,
    document_id=1,
    chunks=chunks
)

db.close()

print("Chunks saved successfully!")