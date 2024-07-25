from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from . import models
from .db_config import SQLALCHEMY_DATABASE_URL


class Dao:
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        models.Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def _add_object(self, object):
        self.db.add(object)
        self.db.commit()
        self.db.refresh(object)
        return object

    def add_student(self, student: models.Student):
        return self._add_object(student)

    def add_subject(self, subject: models.Subject):
        return self._add_object(subject)

    def assign_subjects_to_student(self, student_subjects: list[models.StudentSubject]):
        for student_subject in student_subjects:
            self.db.add(student_subject)
        self.db.commit()

    def add_degree(self, degree: models.Degree):
        return self._add_object(degree)

    def get_student_by_email(self, email: str):
        return (
            self.db.query(models.Student).filter(models.Student.email == email).first()
        )

    def get_student_by_id(self, student_id: int):
        return (
            self.db.query(models.Student)
            .filter(models.Student.id == student_id)
            .first()
        )

    def get_students(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Student).offset(skip).limit(limit).all()

    def get_students_count(self):
        return self.db.query(models.Student).count()

    def get_degrees(self):
        return self.db.query(models.Degree).all()

    def get_degree_by_id(self, degree_id: int):
        return (
            self.db.query(models.Degree).filter(models.Degree.id == degree_id).first()
        )

    def get_subjects_by_degree(self, degree_id: int):
        return (
            self.db.query(models.Subject)
            .filter(models.Subject.degree_id == degree_id)
            .all()
        )

    def get_subjects(self):
        return self.db.query(models.Subject).all()

    def get_subjects_by_ids(self, ids: set):
        return self.db.query(models.Subject).filter(models.Subject.id.in_(ids)).all()

    def get_student_info(self, student_id: int):
        return (
            self.db.query(models.Student)
            .options(joinedload(models.Student.subjects))
            .filter(models.Student.id == student_id)
            .first()
        )

    def get_students_info(self, skip: int = 0, limit: int = 100):
        return (
            self.db.query(models.Student)
            .options(joinedload(models.Student.subjects))
            .offset(skip)
            .limit(limit)
            .all()
        )
