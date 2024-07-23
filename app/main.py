from fastapi import Depends, FastAPI, HTTPException, status
from . import models, schemas
from .controllers import Controller, get_controller
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/students/")
def read_students(skip: int = 0, limit: int = 100, controller: Controller = Depends(get_controller)):
    students = controller.get_students_info(skip=skip, limit=limit)
    count = controller.get_students_count()   
    paginated_students = {
        "items": [student.__dict__ for student in students],
        "skip": skip,
        "limit": limit,
        "total": count}

    return paginated_students

@app.get("/students/{student_id}")
def read_student(student_id: int, controller: Controller = Depends(get_controller)):
    student = controller.get_student_info(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students/", status_code=status.HTTP_201_CREATED)
def create_student(student_info: schemas.StudentInfoBase, controller: Controller = Depends(get_controller)):
    student_with_same_email = controller.get_student_by_email(email=student_info.email)
    if student_with_same_email:
        raise HTTPException(status_code=400, detail="Email already registred")
    
    subjects_ids = {s.subject_id for s in student_info.subjects}
    if not controller.verify_subjects_ids(subjects_ids):
        raise HTTPException(status_code=400, detail="Invalid Subject ids")
    
    student = controller.insert_student_info(student_info)

    return {"student_id": student.id}

@app.get("/subjects/")
def read_degrees(controller: Controller = Depends(get_controller)):
    return controller.get_subjects()

@app.get("/degrees/")
def read_degrees(controller: Controller = Depends(get_controller)):
    return controller.get_degrees()

@app.get("/degrees/{degree_id}/subjects")
def read_degrees(degree_id: int, controller: Controller = Depends(get_controller)):
    degree = controller.get_degree(degree_id)
    if degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return controller.get_degree_subjects(degree_id)

