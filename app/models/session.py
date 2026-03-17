from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Session(Base):
  __tablename__="sessions"
  id=Column(Integer,primary_key=True,index=True)
  start_hour=Column(String)
  end_hour=Column(String)
  status=Column(String)
  date=Column(String)
  service_id=Column(Integer,ForeignKey('services.id'))
  service=relationship("Service", back_populates="sessions")
  teacher_id=Column(Integer,ForeignKey('teachers.id'))
  teacher=relationship("Teacher", back_populates="sessions")
  documents=relationship("Document", back_populates="session")
  students=relationship("Student", secondary=student_session, back_populates="sessions")