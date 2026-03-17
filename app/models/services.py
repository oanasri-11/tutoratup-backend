from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Service(Base):
  __tablename__="services"
  id=Column(Integer,primary_key=True,index=True)
  education_domain=Column(String)
  approximate_price=Column(Integer)
  level=Column(String)
  name=Column(String)
  session=relationship("Session", back_populates="service")
  teacher_id=Column(Integer,ForeignKey('teachers.id'))
  teacher=relationship("Teacher", back_populates="services")
  students=relationship("Student", secondary=student_session, back_populates="services")


