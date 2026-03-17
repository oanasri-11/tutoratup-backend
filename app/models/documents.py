from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Document(Base):
  __tablename__="documents"
  id=Column(Integer,primary_key=True,index=True)
  type=Column(String)
  description=Column(String)
  date=Column(String)
  session_id=Column(Integer,ForeignKey('sessions.id'))
  session=relationship("Session", back_populates="documents")
  