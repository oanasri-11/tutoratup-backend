from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase

class StudentBase(UserBase):
  learning_objectives:str
class StudentCreate(StudentBase):
  password:str
  confirm_password:str
  educational_level:str
  fullname:str
class StudentOut(StudentBase):
  id:int
  parent_id:int
  class Config:
    orm_mode=True  
  
