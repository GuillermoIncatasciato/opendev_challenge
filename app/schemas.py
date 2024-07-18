from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    email: str
    address: str
    phone: int

    class Config:
        orm_mode = True

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True 
    
class Subject(BaseModel):
    name: str
    degree_id: int

class Degree(BaseModel):
    name: str
 
class SubjectInfo(BaseModel):
    subject_id: int
    enrollment_year : int
    times_taken: int

    class config:
        extra = "ignore"

class StudentInfoBase(StudentBase):
    subjects: list[SubjectInfo]

class StudentInfo(Student):
    subjects: list[SubjectInfo]


