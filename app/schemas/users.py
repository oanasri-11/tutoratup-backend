from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  

  Phone_number:int
  Postal_Adress:str
  email:EmailStr
class UserCreate(UserBase):
  password:str
class UserOut(UserBase):
  id:int
  First_name:str
  Last_name:str
  class Config:
    orm_mode=True #tells pydantic to read the data even if it is not a dict, but an ORM model ( SQLAlchemy)   
    