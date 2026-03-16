from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Evaluation(Base):
  __tablename__="evaluations"
  id=Column(Integer,primary_key=True,index=True)
  comment=Column(String)
  date=Column(String)
  note=Column(Float)
  