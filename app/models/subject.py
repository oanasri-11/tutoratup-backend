from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Subject(Base):
  __tablename__="subjects"
  id=Column(Integer,primary_key=True,index=True)
  name=Column(String)
  teachers=relationship("Teacher", back_populates="subject")
  