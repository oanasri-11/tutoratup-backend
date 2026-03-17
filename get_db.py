import os
from app.database.database import engine, Base
# IMPORTANT: You must import all models so SQLAlchemy knows about the tables
from app.models.users import User
from app.models.teacher import Teacher
from app.models.students import Student
from app.models.session import TutoringSession # Or whatever your class name is

print("Current Directory:", os.getcwd())
print("Target Database: mydatabase.db")

try:
    # This command creates the file and the tables
    Base.metadata.create_all(bind=engine)
    print("✅ SUCCESS: 'mydatabase.db' has been created in the root folder!")
except Exception as e:
    print(f"❌ ERROR: {e}")