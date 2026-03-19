from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase
class ParentBase(UserBase):
 pass

class ParentCreate(ParentBase):
  password:str
  confirm_password:str
  fullname:str
class ParentOut(ParentBase):
  id:int
  class Config:
    orm_mode=True  
  





  