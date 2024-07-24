from . import models, schemas
from .repository import Repository


_CONTROLLER = None

class Controller:
    def __init__(self, repo: Repository):
            self.repo = repo

    def create_student(self, student: schemas.StudentBase):
        db_student = models.Student(**student.model_dump())  
        return self.repo.add_student(db_student)

    def create_subject(self, subject: schemas.Subject):
        db_subject = models.Subject(**subject.model_dump())
        return self.repo.add_subject(db_subject)

    def create_degree(self, degree: schemas.Degree):
        db_degree = models.Degree(**degree.model_dump())
        return self.repo.add_degree(db_degree)

    def get_student_by_email(self, email: str):
        return self.repo.get_student_by_email(email)

    def get_student_by_id(self, student_id: int):
        return self.repo.get_student_by_id(student_id)

    def get_students(self, skip: int = 0, limit: int = 100):
        return self.repo.get_student(skip, limit)

    def get_students_count(self):
        return self.repo.get_students_count()

    def get_degrees(self):
        return self.repo.get_degrees()

    def get_degree_by_id(self, degree_id: int):
        return self.repo.get_degree_by_id(degree_id)

    def get_subjects_by_degree(self, degree_id: int):
        return self.repo.get_subjects_by_degree(degree_id)

    def get_subjects(self):
        return self.repo.get_subjects()

    def verify_subjects_ids(self, ids: set):
        existing_ids = {subject.id for subject in self.repo.get_subjects_by_ids(ids)}
        return ids == existing_ids

    def insert_student_info(self, student_info: schemas.StudentInfoBase):
        student_fields = {k: student_info.model_dump()[k] for k in schemas.StudentBase.model_fields.keys()}
        db_student = self.repo.add_student(models.Student(**student_fields))
        student_subjects = [
            models.StudentSubject(student_id=db_student.id, **subject.model_dump())
            for subject in student_info.subjects
        ] 
        
        self.repo.assign_subjects_to_student(student_subjects)

        return db_student

    def get_student_info(self, student_id: int):
        return self.repo.get_student_info(student_id)

    def get_students_info(self, skip: int = 0, limit: int = 100):
        return self.repo.get_students_info(skip, limit)


def get_controller():
    global _CONTROLLER
    if _CONTROLLER is None:
        _CONTROLLER = Controller(Repository())
    return _CONTROLLER

    