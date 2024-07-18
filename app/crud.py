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


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

    

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


"""

def get_students_info(db: Session, skip: int = 0, limit: int = 100):
    query_join_results = (
    db.query(models.Student, models.StudentSubject)
    .join(models.StudentSubject, models.Student.id == models.StudentSubject.student_id)
    .all()
    )
    students_ids = set()
    students = []
    students_subjects = {}

    for student, subject in query_join_results:

        if student.id not in students_ids:
            students_ids.add(student.id)
            print(id)
            print(student.__dict__)
            students.append(student.__dict__)
            students_subjects[student.id] = [subject.__dict__]
        else:
            students_subjects[student.id].appen(subject.__dict__)

    students_info = []

    for student in students:
        subjects = [schemas.SubjectInfo(**subject) for subject in students_subjects[student[id]]]
        students_info.append(schemas.StudentInfo(**student,subjects=subjects))

    return students_info

"""

def get_students_info(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).options(joinedload(models.Student.subjects)).offset(skip).limit(limit).all()