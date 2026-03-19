from pydantic import BaseModel, EmailStr
class teachingLevelBase(BaseModel):
  name:str
class teachingLevelCreate(teachingLevelBase):
  pass  
class teachingLevelOut(teachingLevelBase):
  id:int
  class Config:
    orm_mode=True  