from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text_from_pdf(filepath:str)->str:
    reader = PdfReader(filepath)

    text=""
    for page in reader.pages:
        page_text=page.extract_text()

        if page_text:
            text+=page_text+"/n"
    return text.strip()

def split_text_into_chunks(text:str):
    splitter=RecursiveCharacterTextSplitter( 
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = splitter.split_text(text)

    return chunks