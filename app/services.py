from . import models, schemas
from .daos import Dao


_SERVICE = None

class Service:
    def __init__(self, dao: Dao):
            self.dao = dao

    def create_student(self, student: schemas.StudentBase):
        db_student = models.Student(**student.model_dump())  
        return self.dao.add_student(db_student)

    def create_subject(self, subject: schemas.Subject):
        db_subject = models.Subject(**subject.model_dump())
        return self.dao.add_subject(db_subject)

    def create_degree(self, degree: schemas.Degree):
        db_degree = models.Degree(**degree.model_dump())
        return self.dao.add_degree(db_degree)

    def get_student_by_email(self, email: str):
        return self.dao.get_student_by_email(email)

    def get_student_by_id(self, student_id: int):
        return self.dao.get_student_by_id(student_id)

    def get_students(self, skip: int = 0, limit: int = 100):
        return self.dao.get_students(skip, limit)

    def get_students_count(self):
        return self.dao.get_students_count()

    def get_degrees(self):
        return self.dao.get_degrees()

    def get_degree_by_id(self, degree_id: int):
        return self.dao.get_degree_by_id(degree_id)

    def get_subjects_by_degree(self, degree_id: int):
        return self.dao.get_subjects_by_degree(degree_id)

    def get_subjects(self):
        return self.dao.get_subjects()

    def verify_subjects_ids(self, ids: set):
        existing_ids = {subject.id for subject in self.dao.get_subjects_by_ids(ids)}
        return ids == existing_ids

    def insert_student_info(self, student_info: schemas.StudentInfoBase):
        student_fields = {k: student_info.model_dump()[k] for k in schemas.StudentBase.model_fields.keys()}
        db_student = self.dao.add_student(models.Student(**student_fields))
        student_subjects = [
            models.StudentSubject(student_id=db_student.id, **subject.model_dump())
            for subject in student_info.subjects
        ] 
        
        self.dao.assign_subjects_to_student(student_subjects)

        return db_student

    def get_student_info(self, student_id: int):
        return self.dao.get_student_info(student_id)

    def get_students_info(self, skip: int = 0, limit: int = 100):
        return self.dao.get_students_info(skip, limit)


def get_service():
    global _SERVICE
    if _SERVICE is None:
        _SERVICE = Service(Dao())
    return _SERVICE

    