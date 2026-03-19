from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase
class QuoteBase(BaseModel):
  objectif:str
  frequence:str
  duration:str
  budget:float
  subject:str
  level:str
  teacher_id:int
class QuoteCreate(QuoteBase):
  pass
class QuoteOut(QuoteBase):
  id:int
  
  class Config:
    orm_mode=True 