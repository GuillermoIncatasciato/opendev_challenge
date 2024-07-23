from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from .database import get_db

_CONTROLLER = None

class Controller:
    def __init__(self, db: Session):
            self.db = db

    def create_student(self, student: schemas.StudentBase):
        db_student = models.Student(**student.model_dump())
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def create_subject(self, subject: schemas.Subject):
        db_subject = models.Subject(**subject.model_dump())
        self.db.add(db_subject)
        self.db.commit()
        self.db.refresh(db_subject)
        return db_subject

    def create_degree(self, degree: schemas.Degree):
        db_degree = models.Degree(**degree.model_dump())
        self.db.add(db_degree)
        self.db.commit()
        self.db.refresh(db_degree)
        return db_degree

    def get_student_by_email(self, email: str):
        return self.db.query(models.Student).filter(models.Student.email == email).first()

    def get_student(self, student_id: int):
        return self.db.query(models.Student).filter(models.Student.id == student_id).first()

    def get_students(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Student).offset(skip).limit(limit).all()

    def get_students_count(self):
        return self.db.query(models.Student).count()

    def get_degrees(self):
        return self.db.query(models.Degree).all()

    def get_degree(self, degree_id: int):
        return self.db.query(models.Degree).filter(models.Degree.id == degree_id).first()

    def get_degree_subjects(self, degree_id: int):
        return self.db.query(models.Subject).filter(models.Subject.degree_id == degree_id).all()

    def get_subjects(self):
        return self.db.query(models.Subject).all()

    def get_subjects_by_ids(self, ids: set):
        return self.db.query(models.Subject).filter(models.Subject.id.in_(ids)).all()

    def verify_subjects_ids(self, ids: set):
        existing_ids = {subject.id for subject in self.get_subjects_by_ids(ids)}
        return ids == existing_ids

    def insert_student_info(self, student_info: schemas.StudentInfoBase):
        student_fields = {k: student_info.model_dump()[k] for k in schemas.StudentBase.model_fields.keys()}
        db_student = models.Student(**student_fields)
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)

        for subject in student_info.subjects:
            db_subject = models.StudentSubject(student_id=db_student.id, **subject.model_dump())
            self.db.add(db_subject)
        self.db.commit()

        return db_student

    def get_student_info(self, student_id: int):
        return self.db.query(models.Student).options(joinedload(models.Student.subjects)).filter(models.Student.id == student_id).first()

    def get_students_info(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Student).options(joinedload(models.Student.subjects)).offset(skip).limit(limit).all()


def get_controller():
    global _CONTROLLER
    if _CONTROLLER is None:
        _CONTROLLER = Controller(get_db())
    return _CONTROLLER

    