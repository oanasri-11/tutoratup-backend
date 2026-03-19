from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase
class DocumentBase(BaseModel):
  type:str
  description:str
  date:str
  session_id:int
class DocumentCreate(DocumentBase):
  pass
class DocumentOut(DocumentBase):
  id:int
  class Config:
    orm_mode=True  