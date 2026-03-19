from app.database.database import engine, Base
from app.database.database import SessionLocal
from app.models.users import User
from app.models.teacher import Teacher
from app.models.students import Student
from app.models.parents import Parent
from app.models.session import Session
from app.models.services import Service
from app.models.quotes import Quote
from app.models.evaluation import Evaluation
from app.models.subject import Subject
from app.models.teachinglevels import TeachingLevel
from app.models.documents import Document
from app.models.association_student_document import student_document
from app.models.association_teacher_student import teacher_student
from app.models.association_student_service import student_service
from app.models.association_student_session import student_session
from app.models.association_student_quote import student_quote

# Create all tables
Base.metadata.create_all(bind=engine)
print("Database and tables created successfully!")
session=SessionLocal()
#never create user automatically, only parent ,student or teacher
s5=Student (

First_name="John",
Last_name="Doe",
email="john.doe@example.com",
Phone_number="1234567890"



)
session.add(s5)
session.commit()












print("Data inserted successfully!")




