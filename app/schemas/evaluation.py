from pydantic import BaseModel, EmailStr
from sqlalchemy import Float
from app.schemas.users import UserBase
class EvaluationBase(BaseModel):
  comment:str
  date:str
  note:str
  teacher_id:int
class EvaluationCreate(EvaluationBase):
  pass
class EvaluationOut(EvaluationBase):
  id:int
  class Config:
    orm_mode=True