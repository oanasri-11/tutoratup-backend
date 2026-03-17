from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.users import User
class Student(User):
  __tablename__="students"
  id=Column(Integer,primary_key=True,index=True)
  learning_objectives=Column(String)

  parent_id=Column(Integer, ForeignKey('parents.id'))
  parent=relationship("Parent", back_populates="students")
  teacher=relationship("Teacher",secondary=teacher_student, back_populates="students")

__mapper_args__ = {
        'polymorphic_identity': 'Student',
    }