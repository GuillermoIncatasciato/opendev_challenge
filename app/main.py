from fastapi import Depends, FastAPI, HTTPException
from . import schemas
from .services import Service, get_service
from .controllers import StudentController

app = FastAPI()


student_controller = StudentController()
app.include_router(student_controller.router)

@app.get("/subjects/")
def read_degrees(service: Service = Depends(get_service)):
    return service.get_subjects()

@app.get("/degrees/")
def read_degrees(service: Service = Depends(get_service)):
    return service.get_degrees()

@app.get("/degrees/{degree_id}/subjects")
def read_degrees(degree_id: int, service: Service = Depends(get_service)):
    degree = service.get_degree_by_id(degree_id)
    if degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return service.get_subjects_by_degree(degree_id)

