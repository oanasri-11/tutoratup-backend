from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Student(User):
  __tablename__="students"
  id=Column(Integer,primary_key=True,index=True)
  learning_objectives=Column(String)
__mapper_args__ = {
        'polymorphic_identity': 'Student',
    }