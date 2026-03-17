from sqlalchemy import Column, Integer, ForeignKey,Table
from app.database.database import Base
student_service = Table(
    "student_service",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("service_id", Integer, ForeignKey("services.id"), primary_key=True),
)