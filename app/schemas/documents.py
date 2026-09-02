from pydantic import BaseModel,EmailStr

class DocumentResponse(BaseModel):
    id:int
    filename:str
    file_path:str
    user_id:int

    class Config:
        from_attributes = True