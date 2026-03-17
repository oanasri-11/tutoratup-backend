from sqlalchemy import Column, Integer, ForeignKey,Table
from app.database.database import Base
student_document=Table(
    "student_document", 
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("document_id", Integer, ForeignKey("documents.id"), primary_key=True)
)