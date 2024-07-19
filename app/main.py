from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas, crud

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students/")
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students_info(db, skip=skip, limit=limit)
    count = crud.get_students_count(db)   
    paginated_students = {
        "items": [student.__dict__ for student in students],
        "skip": skip,
        "limit": limit,
        "total": count}

    return paginated_students

@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_info(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students/", status_code=status.HTTP_201_CREATED)
def create_student(student_info: schemas.StudentInfoBase, db: Session = Depends(get_db)):
    student_with_same_email = crud.get_student_by_email(db, email=student_info.email)
    if student_with_same_email:
        raise HTTPException(status_code=400, detail="Email already registred")
    
    subjects_ids = {s.subject_id for s in student_info.subjects}
    if not crud.verify_subjects_ids(db, subjects_ids):
        raise HTTPException(status_code=400, detail="Invalid Subject ids")
    
    student = crud.insert_student_info(db, student_info)

    return {"student_id": student.id}
