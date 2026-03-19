from pydantic import BaseModel, EmailStr
from app.schemas.subject import SubjectOut
from app.schemas.teachinglevels import teachingLevelOut
from app.schemas.teachinglevels import teachingLevelOut
from app.schemas.users import UserBase
class TeacherBase(UserBase):
  education_level:str
  location_mode:str
  geolocation:str
  deplacemnt:str
  nature:str
  domain:str

class TeacherCreate(TeacherBase):
  Fullname:str
  password:str
  confirm_password:str
  profile_picture:str
  travel_capacity:str
  bio:str
  certificates:str
  subjects:list[int]
  teaching_levels:list[int]
class TeacherOut(TeacherBase):
  id:int
  subjects:list[SubjectOut]
  teaching_levels:list[teachingLevelOut]
  class Config:
    orm_mode=True  


