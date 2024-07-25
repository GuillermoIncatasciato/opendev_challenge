from fastapi import FastAPI
from .controllers import StudentController, DegreeController, SubjectController


student_controller = StudentController()
degree_controller = DegreeController()
subject_controller = SubjectController()

app = FastAPI()
app.include_router(student_controller.router, tags=["student"])
app.include_router(degree_controller.router, tags=["degree"])
app.include_router(subject_controller.router, tags=["subject"])