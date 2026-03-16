from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Session(Base):
  __tablename__="sessions"
  id=Column(Integer,primary_key=True,index=True)
  start_hour=Column(String)
  end_hour=Column(String)
  status=Column(String)
  date=Column(String)
