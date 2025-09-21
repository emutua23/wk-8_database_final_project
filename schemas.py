# schemas.py
from pydantic import BaseModel
from typing import List, Optional

# Student Schemas
class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    name: Optional[str] = None
    email: Optional[str] = None

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True  # This replaces 'orm_mode' in older Pydantic versions

# Course Schemas
class CourseBase(BaseModel):
    title: str
    student_id: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    title: Optional[str] = None
    student_id: Optional[int] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True