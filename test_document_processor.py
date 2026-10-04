from app.services.document_services import (
    extract_text_from_pdf,
    split_text_into_chunks
)

file_path="uploads/Company_Search.pdf"

text = extract_text_from_pdf(file_path)

chunks=split_text_into_chunks(text)

print("========== EXTRACTED TEXT ==========")
print(text)
for index, chunk in enumerate(chunks, start=1):
    print(f"\n========== CHUNK {index} ==========")
    print(chunk)
print("====================================")
