from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import relationship  
class Teacher(User):
  __tablename__="teachers"
  id=Column(Integer,primary_key=True,index=True)
  education_level=Column(String)
  location_mode=Column(   String  )
  geolocation=Column(String)
  deplacemnt=Column(String)
  nature=Column(String)
  domain=Column(String)
  quotes=relationship("Quote", back_populates="teacher")
  teachers=relationship("Service", back_populates="teacher")
  subject_id=Column(Integer,ForeignKey('subjects.id'))
  subject=relationship("Subject", back_populates="teachers")
  evaluations=relationship("Evaluation", back_populates="teacher")
  students=relationship("Student",secondary=teacher_student, back_populates="teacher")

__mapper_args__ = {
        'polymorphic_identity': 'Teacher',
    }