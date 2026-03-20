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
from app.schemas.users import UserCreate
from app.schemas.teacher import TeacherCreate 
from app.schemas.students import StudentCreate
from app.schemas.parents import ParentCreate
from app.schemas.session import SessionCreate
from app.schemas.services import ServiceCreate
from app.schemas.quotes import QuoteCreate
from app.schemas.evaluation import EvaluationCreate
from app.schemas.subject import SubjectCreate
from app.schemas.teachinglevels import teachingLevelCreate
from app.schemas.documents import DocumentCreate


# Create all tables
#Base.metadata.create_all(bind=engine)
#print("Database and tables created successfully!")
#session=SessionLocal()
#never create user automatically, only parent ,student or teacher
print ("Testing pydantic without database !!!!!!!!")
data ={
    "email":"testeexample",
    "password":"testpassword",
    "fullname":"59988989889",
    "confirm_password":"testpassword",
}
    
student=StudentCreate(**data)
print(student)








    




