from sqlalchemy import Column, Integer, ForeignKey,Table
from app.database.database import Base
teacher_student=  Table('teacher_student',Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teachers.id'),primary_key=True),
    Column('student_id', Integer, ForeignKey('students.id'),primary_key=True)
)