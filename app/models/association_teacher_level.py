from sqlalchemy import Column, Integer, ForeignKey,Table
from app.database.database import Base
teacher_levels = Table('teacher_levels', Base.metadata,
    Column('teacher_id', ForeignKey('teachers.id'), primary_key=True),
    Column('level_id', ForeignKey('levels.id'), primary_key=True)
)