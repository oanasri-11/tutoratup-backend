from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Service(Base):
  __tablename__="services"
  id=Column(Integer,primary_key=True,index=True)
  education_domain=Column(String)
  approximate_price=Column(Integer)
  level=Column(String)
  name=Column(String)


