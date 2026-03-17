from sqlalchemy import Table, Column, ForeignKey, Integer
from app.database.database import Base
student_quote=  Table('student_quote',Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'),primary_key=True),
    Column('quote_id', Integer, ForeignKey('quotes.id'),primary_key=True)
)