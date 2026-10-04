from app.services.document_services import extract_text_from_pdf

file_path="uploads/Company_Search.pdf"

text = extract_text_from_pdf(file_path)

print("========== EXTRACTED TEXT ==========")
print(text)
print("====================================")
