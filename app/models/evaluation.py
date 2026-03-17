from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Evaluation(Base):
  __tablename__="evaluations"
  id=Column(Integer,primary_key=True,index=True)
  comment=Column(String)
  date=Column(String)
  note=Column(Float)
  teacher_id=Column(Integer,ForeignKey('teachers.id'))
  teacher=relationship("Teacher", back_populates="evaluations")
  