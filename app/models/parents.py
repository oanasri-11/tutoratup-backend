from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base
from app.models.users import User
class Parent(User):
  __tablename__="parents"
  id=Column(Integer,primary_key=True,index=True)
  referent_children=Column(String)


  
__mapper_args__ = {
        'polymorphic_identity': 'parent',
    }