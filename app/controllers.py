from fastapi import APIRouter, HTTPException, status
from . import schemas
from .services import get_service



class StudentController:

    def __init__(self):
        self.router = APIRouter()
        self.service = get_service()
        self.router.add_api_route("/students/", self.read_students, methods=["GET"])
        self.router.add_api_route("/students/{student_id}", self.read_student, methods=["GET"])
        self.router.add_api_route("/students/", self.create_student, methods=["POST"], status_code=status.HTTP_201_CREATED)


    def read_students(self, skip: int = 0, limit: int = 100):
        students = self.service.get_students_info(skip=skip, limit=limit)
        count = self.service.get_students_count()   
        paginated_students = {
            "items": [student.__dict__ for student in students],
            "skip": skip,
            "limit": limit,
            "total": count}

        return paginated_students
    
    def read_student(self, student_id: int):
        student = self.service.get_student_info(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student


    def create_student(self, student_info: schemas.StudentInfoBase):
        student_with_same_email = self.service.get_student_by_email(email=student_info.email)
        if student_with_same_email:
            raise HTTPException(status_code=400, detail="Email already registred")
        
        subjects_ids = {s.subject_id for s in student_info.subjects}
        if not self.service.verify_subjects_ids(subjects_ids):
            raise HTTPException(status_code=400, detail="Invalid Subject ids")
        
        student = self.service.insert_student_info(student_info)

        return {"student_id": student.id}
