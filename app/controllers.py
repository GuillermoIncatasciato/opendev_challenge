from fastapi import APIRouter, HTTPException, status
from . import schemas
from .services import get_service


class Controller:
    def __init__(self):
        self.router = APIRouter()
        self.service = get_service()

class StudentController(Controller):

    def __init__(self):
        super().__init__()
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


class DegreeController(Controller):

    def __init__(self):
        super().__init__()
        self.router.add_api_route("/degrees/", self.read_degrees, methods=["GET"])
        self.router.add_api_route("/degrees/{degree_id}/subjects", self.read_subjects_by_degree, methods=["GET"])

    def read_degrees(self):
        return self.service.get_degrees()

    def read_subjects_by_degree(self, degree_id: int):
        degree = self.service.get_degree_by_id(degree_id)
        if degree is None:
            raise HTTPException(status_code=404, detail="Degree not found")
        return self.service.get_subjects_by_degree(degree_id)


class SubjectController(Controller):
    def __init__(self):
        super().__init__()
        self.router.add_api_route("/subjects/", self.read_subjects, methods=["GET"])

    def read_subjects(self):
        return self.service.get_subjects()



    

