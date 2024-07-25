from fastapi import FastAPI, APIRouter
from .controllers import StudentController, DegreeController, SubjectController
from .services import Service
from .daos import Dao

service = Service(Dao())
router = APIRouter()

student_controller = StudentController(service, router) 
degree_controller = DegreeController(service, router)
subject_controller = SubjectController(service, router)

app = FastAPI()

app.include_router(student_controller.router, tags=["student"])
app.include_router(degree_controller.router, tags=["degree"])
app.include_router(subject_controller.router, tags=["subject"])
