from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase
class ServiceBase(BaseModel):
  education_domain:str
  approximate_price:int
  level:str
  name:str
  
  teacher_id:int
  
class ServiceCreate(ServiceBase):
  pass
class ServiceOut(ServiceBase):
  id:int
  class Config:
    orm_mode=True  
