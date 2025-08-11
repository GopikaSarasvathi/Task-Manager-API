from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv 

load_dotenv()
# Load the database URL from environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
from sqlalchemy import text

# Test DB connection
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Database connection successful")
except Exception as e:
    print("❌ Database connection failed:", e)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
