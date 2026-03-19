from sqlalchemy import Column, Integer, ForeignKey,Table
from app.database.database import Base

teacher_subjects = Table('teacher_subjects', Base.metadata,
    Column('teacher_id', ForeignKey('teachers.id'), primary_key=True),
    Column('subject_id', ForeignKey('subjects.id'), primary_key=True)
)