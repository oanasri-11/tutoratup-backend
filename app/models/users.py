from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base

Base=declarative_base()

class User(Base):
  __tablename__="users"
  id=Column(Integer,primary_key=True,index=True)
  First_name=Column(String)
  Last_name=Column(String)
  email=Column(String, unique=True, index=True)
  Phone_number=Column(Integer)
  Postal_Adress=Column(String)
  role=Column(String)

  # This 'type' column tells SQLAlchemy how to handle inheritance
  type = Column(String)

__mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type,
    }
  
