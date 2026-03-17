from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
from app.models.association_student_service import student_service
class Service(Base):
  __tablename__="services"
  id=Column(Integer,primary_key=True,index=True)
  education_domain=Column(String)
  approximate_price=Column(Integer)
  level=Column(String)
  name=Column(String)
  sessions=relationship("Session", back_populates="service")
  teacher_id=Column(Integer,ForeignKey('teachers.id'))
  teacher=relationship("Teacher", back_populates="services")
  students=relationship("Student", secondary=student_service, back_populates="services")


