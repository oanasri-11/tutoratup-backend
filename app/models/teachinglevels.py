from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class TeachingLevel(Base):
  __tablename__="teaching_levels"
  id=Column(Integer,primary_key=True,index=True)
  name=Column(String)
  teachers=relationship("Teacher", back_populates="teachinglevel")
  