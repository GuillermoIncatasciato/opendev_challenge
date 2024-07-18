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
    return students

@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student_info = crud.get_student_info(db, student_id)
    if db_student_info is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student_info

@app.post("/students/", status_code=status.HTTP_201_CREATED)
def create_student(student_info: schemas.StudentInfoBase, db: Session = Depends(get_db)):
    student = crud.insert_student_info(db, student_info)
    return { "id ": student.id, "success": True}
    
    


"""
@app.post("/students/")
def create_student(student: schemas.StudentBase, db : Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students/")
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

"""
@app.get("/health-check/")
def check():
    return {"success": True}


