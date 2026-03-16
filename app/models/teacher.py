from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Teacher(User):
  __tablename__="teachers"
  id=Column(Integer,primary_key=True,index=True)
  education_level=Column(String)
  location_mode=Column(   String  )
  geolocation=Column(String)
  deplacemnt=Column(String)
  nature=Column(String)
  domain=Column(String)

__mapper_args__ = {
        'polymorphic_identity': 'Teacher',
    }