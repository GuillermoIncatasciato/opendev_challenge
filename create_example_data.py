from app.database import SessionLocal
from app import crud, schemas

degree_subjects = {
    "Medicina": [
        "Anatomía",
        "Fisiología",
        "Bioquímica",
        "Farmacología",
        "Patología"
    ],
    "Ingeniería Civil": [
        "Mecánica de Suelos",
        "Estructuras",
        "Hidráulica",
        "Topografía",
        "Construcción"
    ],
    "Derecho": [
        "Derecho Constitucional",
        "Derecho Penal",
        "Derecho Civil",
        "Derecho Administrativo",
        "Derecho Internacional"
    ]
}

students = [
    {
        "name": "Ana García",
        "email": "ana.garcia@example.com",
        "address": "Calle Independencia 456, Ciudad",
        "phone": 111222333,
        "subjects": [
            {"subject_id": 1, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 5, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 10, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Pedro Martínez",
        "email": "pedro.martinez@example.com",
        "address": "Avenida Libertad 789, Pueblo",
        "phone": 444555666,
        "subjects": [
            {"subject_id": 3, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 7, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 12, "enrollment_year": 2019, "times_taken": 1}
        ]
    },
    {
        "name": "Laura Rodríguez",
        "email": "laura.rodriguez@example.com",
        "address": "Plaza Principal 123, Villa",
        "phone": 777888999,
        "subjects": [
            {"subject_id": 2, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 6, "enrollment_year": 2020, "times_taken": 1},
            {"subject_id": 11, "enrollment_year": 2021, "times_taken": 2}
        ]
    },
    {
        "name": "Miguel López",
        "email": "miguel.lopez@example.com",
        "address": "Ruta Nacional 101, Campo",
        "phone": 123456789,
        "subjects": [
            {"subject_id": 4, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 8, "enrollment_year": 2019, "times_taken": 1},
            {"subject_id": 13, "enrollment_year": 2021, "times_taken": 3}
        ]
    },
    {
        "name": "Sofía Fernández",
        "email": "sofia.fernandez@example.com",
        "address": "Avenida Central 567, Aldea",
        "phone": 987654321,
        "subjects": [
            {"subject_id": 9, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 14, "enrollment_year": 2019, "times_taken": 2},
            {"subject_id": 15, "enrollment_year": 2020, "times_taken": 1}
        ]
    }
]

db = SessionLocal()

for degree, subjects in degree_subjects.items():
    
    degree_db = crud.create_degree(db, schemas.Degree(name=degree))

    for subject in subjects: 
        crud.create_subject(db, schemas.Subject(name=subject, degree_id=degree_db.id))


for student in students:
    crud.insert_student_info(db, schemas.StudentInfoBase(**student))