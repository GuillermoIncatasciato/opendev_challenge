from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    phone = Column(Integer)

    subjects = relationship("StudentSubject")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    degree_id = Column(Integer, ForeignKey("degrees.id"))

class Degree(Base):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

class StudentSubject(Base):
    __tablename__ = "students_subjects"

    student_id = Column(ForeignKey('students.id'), primary_key=True)
    subject_id = Column(ForeignKey('subjects.id'), primary_key=True)
    times_taken = Column(Integer)
    enrollment_year = Column(Integer)