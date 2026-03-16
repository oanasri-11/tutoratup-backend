from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Quote(Base):
  __tablename__="quotes"
  id=Column(Integer,primary_key=True,index=True)
  objectif=Column(String)
  frequence=Column(String)
  duration=Column(String)
  budget=Column(Float)
  subject=Column(String)
  level=Column(String)