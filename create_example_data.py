from app.database import SessionLocal
from app import crud, schemas


db = SessionLocal()

med = crud.create_degree(db, schemas.Degree(name="Medicina"))
ing = crud.create_degree(db, schemas.Degree(name="Ingeniería"))
cse = crud.create_degree(db, schemas.Degree(name="Ciencias Economica"))
psi = crud.create_degree(db, schemas.Degree(name="Psicología"))

crud.create_subject(db, schemas.Subject(name="Anatomía", degree_id=med.id))





