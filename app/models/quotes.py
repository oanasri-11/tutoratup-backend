from sqlalchemy import Column, Integer, String,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
from app.models.association_student_quote import student_quote
class Quote(Base):
  __tablename__="quotes"
  id=Column(Integer,primary_key=True,index=True)
  objectif=Column(String)
  frequence=Column(String)
  duration=Column(String)
  budget=Column(Float)
  subject=Column(String)
  level=Column(String)
  teacher_id=Column(Integer,ForeignKey('teachers.id'))
  teacher=relationship("Teacher", back_populates="quotes")
  students=relationship("Student", secondary=student_quote, back_populates="quotes")