# database.py
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

pymysql.install_as_MySQLdb()

# Get database credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "crud_app_db")

SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# Create the engine
# For MySQL, we don't need the `check_same_thread` argument.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # Optional: Echo SQL queries to console for debugging
    # echo=True
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

# Define your models (same as before)
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)

    # Define the reverse relationship
    courses = relationship("Course", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    student_id = Column(Integer, ForeignKey("students.id"))

    # Define the relationship
    student = relationship("Student", back_populates="courses")
