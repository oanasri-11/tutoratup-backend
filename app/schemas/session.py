from pydantic import BaseModel, EmailStr
from app.schemas.users import UserBase
class SessionBase(BaseModel):
  start_hour:str
  teacher_id:int
  student_id:int
  
  end_hour:str
  status:str
  date:str
class SessionCreate(SessionBase):
  pass
class SessionOut(SessionBase):
  id:int


