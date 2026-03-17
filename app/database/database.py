from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite connection (file will be created automatically)
SQLALCHEMY_DATABASE_URL = "sqlite:///./mydatabase.db"  

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} 
)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes/services
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test connection 
if __name__ == "__main__":
    try:
        connection = engine.connect()
        print(" Connected to SQLite successfully!")
        connection.close()
    except Exception as e:
        print(" Connection failed:", e)