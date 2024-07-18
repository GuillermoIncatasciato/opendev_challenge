from sqlalchemy.orm import Session, joinedload

from . import models, schemas

def create_student(db: Session, student: schemas.StudentBase):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_subject(db: Session, subject: schemas.Subject):
    db_subject = models.Subject(**subject.model_dump())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def create_degree(db: Session, degree: schemas.Degree):
    db_degree = models.Degree(**degree.model_dump())
    db.add(db_degree)
    db.commit()
    db.refresh(db_degree)
    return db_degree

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_students_count(db: Session):
    return db.query(models.Student).count()

def get_subjects_by_id(db: Session, ids: set):
    return db.query(models.Subject).filter(models.Subject.id.in_(ids)).all()

def verify_subjects_ids(db: Session, ids: set):
    existing_ids = {subject.id for subject in get_subjects_by_id(db, ids)}
    return ids == existing_ids

def insert_student_info(db: Session, student_info: schemas.StudentInfoBase):

    student_fields = {k: student_info.model_dump()[k] for k in schemas.StudentBase.model_fields.keys()}
    db_student = models.Student(**student_fields)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    for subject in student_info.subjects:
        db_subject = models.StudentSubject(student_id=db_student.id, **subject.model_dump())
        db.add(db_subject)   
    db.commit()
    
    return db_student

def get_student_info(db: Session, student_id: int):
    return db.query(models.Student).options(joinedload(models.Student.subjects)).filter(models.Student.id == student_id).first()


def get_students_info(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).options(joinedload(models.Student.subjects)).offset(skip).limit(limit).all()
