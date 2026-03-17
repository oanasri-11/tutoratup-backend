from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import relationship  
from app.models.association_teacher_student import teacher_student

class Teacher(User):
  __tablename__="teachers"
  id=Column(Integer, ForeignKey('users.id'), primary_key=True)
  education_level=Column(String)
  location_mode=Column(   String  )
  geolocation=Column(String)
  deplacemnt=Column(String)
  nature=Column(String)
  domain=Column(String)
  quotes=relationship("Quote", back_populates="teacher")
  services=relationship("Service", back_populates="teacher")
  sessions=relationship("Session", back_populates="teacher")
  subject_id=Column(Integer,ForeignKey('subjects.id'))
  subject=relationship("Subject", back_populates="teachers")
  evaluations=relationship("Evaluation", back_populates="teacher")
  students=relationship("Student",secondary=teacher_student, back_populates="teacher")
  teachinglevel_id=Column(Integer,ForeignKey('teaching_levels.id'))
  teachinglevel=relationship("TeachingLevel", back_populates="teachers")

  __mapper_args__ = {
        'polymorphic_identity': 'Teacher',
    }