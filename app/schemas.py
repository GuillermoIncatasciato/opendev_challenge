from pydantic import BaseModel, EmailStr, field_validator


class StudentBase(BaseModel):
    name: str
    email: EmailStr
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

    @field_validator('subjects')
    def different_subjects(cls, value):
        id_subjects = {subject_info.subject_id for subject_info in value}
        if len(value) != len(id_subjects):
            raise ValueError("Subjects should be different")
        return value
        
        

class StudentInfo(Student):
    subjects: list[SubjectInfo]


