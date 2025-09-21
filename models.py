# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"
    __table_args__ = {'extend_existing': True}  # <-- ADD THIS LINE

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)

    courses = relationship("Course", back_populates="student")


class Course(Base):
    __tablename__ = "courses"
    __table_args__ = {'extend_existing': True}  # <-- ADD THIS LINE

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="courses")