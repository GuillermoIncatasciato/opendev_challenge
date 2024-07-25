from app import schemas
from app.services import get_service

degree_subjects = {
    "Ingeniería en Computación": [
        "Algoritmos y Estructuras de Datos",
        "Bases de Datos",
        "Programación Funcional",
        "Sistemas Operativos",
        "Redes de Computadoras"
    ],
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
    ],
    "Psicología": [
        "Psicología General",
        "Psicología del Desarrollo",
        "Psicología Clínica",
        "Psicología Educativa",
        "Psicología Social"
    ],
    "Administración de Empresas": [
        "Fundamentos de Administración",
        "Contabilidad Financiera",
        "Marketing",
        "Finanzas Corporativas",
        "Gestión de Recursos Humanos"
    ],
    "Biología": [
        "Biología Celular",
        "Genética",
        "Ecología",
        "Microbiología",
        "Biología Molecular"
    ],
    "Química": [
        "Química General",
        "Química Orgánica",
        "Química Inorgánica",
        "Fisicoquímica",
        "Química Analítica"
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
        "name": "Carlos Pérez",
        "email": "carlos.perez@example.com",
        "address": "Avenida Libertad 789, Ciudad",
        "phone": 222333444,
        "subjects": [
            {"subject_id": 2, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 6, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 15, "enrollment_year": 2022, "times_taken": 1}
        ]
    },
    {
        "name": "Beatriz López",
        "email": "beatriz.lopez@example.com",
        "address": "Calle Falsa 123, Ciudad",
        "phone": 333444555,
        "subjects": [
            {"subject_id": 3, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 8, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 20, "enrollment_year": 2020, "times_taken": 2}
        ]
    },
    {
        "name": "David Gómez",
        "email": "david.gomez@example.com",
        "address": "Pasaje Flores 456, Ciudad",
        "phone": 444555666,
        "subjects": [
            {"subject_id": 4, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 12, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 25, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Elena Rodríguez",
        "email": "elena.rodriguez@example.com",
        "address": "Calle Central 789, Ciudad",
        "phone": 555666777,
        "subjects": [
            {"subject_id": 7, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 14, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 30, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Fernando Ramírez",
        "email": "fernando.ramirez@example.com",
        "address": "Avenida Principal 123, Ciudad",
        "phone": 666777888,
        "subjects": [
            {"subject_id": 9, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 16, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 35, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Gabriela Hernández",
        "email": "gabriela.hernandez@example.com",
        "address": "Calle Nueva 456, Ciudad",
        "phone": 777888999,
        "subjects": [
            {"subject_id": 11, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 18, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 40, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Hugo Vargas",
        "email": "hugo.vargas@example.com",
        "address": "Calle Luna 789, Ciudad",
        "phone": 888999000,
        "subjects": [
            {"subject_id": 13, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 19, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 29, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Isabel Torres",
        "email": "isabel.torres@example.com",
        "address": "Avenida Estrella 456, Ciudad",
        "phone": 999000111,
        "subjects": [
            {"subject_id": 17, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 22, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 34, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Jorge Ruiz",
        "email": "jorge.ruiz@example.com",
        "address": "Calle Sol 123, Ciudad",
        "phone": 300111222,
        "subjects": [
            {"subject_id": 21, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 24, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 36, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Karina Morales",
        "email": "karina.morales@example.com",
        "address": "Avenida Luna 789, Ciudad",
        "phone": 111222333,
        "subjects": [
            {"subject_id": 26, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 27, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 33, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Luis Rojas",
        "email": "luis.rojas@example.com",
        "address": "Calle Estrella 456, Ciudad",
        "phone": 222333444,
        "subjects": [
            {"subject_id": 23, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 28, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 32, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "María Castillo",
        "email": "maria.castillo@example.com",
        "address": "Avenida Sol 789, Ciudad",
        "phone": 333444555,
        "subjects": [
            {"subject_id": 31, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 37, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 38, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Natalia Soto",
        "email": "natalia.soto@example.com",
        "address": "Calle Luna 123, Ciudad",
        "phone": 444555666,
        "subjects": [
            {"subject_id": 2, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 5, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 11, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Oscar Gil",
        "email": "oscar.gil@example.com",
        "address": "Avenida Libertad 456, Ciudad",
        "phone": 555666777,
        "subjects": [
            {"subject_id": 6, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 9, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 14, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Paula Ramírez",
        "email": "paula.ramirez@example.com",
        "address": "Calle Independencia 789, Ciudad",
        "phone": 666777888,
        "subjects": [
            {"subject_id": 4, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 10, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 19, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Ricardo Vargas",
        "email": "ricardo.vargas@example.com",
        "address": "Avenida Principal 123, Ciudad",
        "phone": 777888999,
        "subjects": [
            {"subject_id": 3, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 8, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 13, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Silvia Ortiz",
        "email": "silvia.ortiz@example.com",
        "address": "Calle Nueva 456, Ciudad",
        "phone": 888999000,
        "subjects": [
            {"subject_id": 7, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 12, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 17, "enrollment_year": 2021, "times_taken": 1}
        ]
    },
    {
        "name": "Tomás Pérez",
        "email": "tomas.perez@example.com",
        "address": "Avenida Estrella 789, Ciudad",
        "phone": 999000111,
        "subjects": [
            {"subject_id": 20, "enrollment_year": 2021, "times_taken": 1},
            {"subject_id": 22, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 25, "enrollment_year": 2019, "times_taken": 3}
        ]
    },
    {
        "name": "Úrsula Herrera",
        "email": "ursula.herrera@example.com",
        "address": "Calle Sol 456, Ciudad",
        "phone": 100111222,
        "subjects": [
            {"subject_id": 23, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 24, "enrollment_year": 2019, "times_taken": 3},
            {"subject_id": 26, "enrollment_year": 2021, "times_taken": 1}
        ]
    }
]


def create_data(degree_subjects, students):
    service = get_service()
    for degree, subjects in degree_subjects.items():

        degree_db = service.create_degree(schemas.Degree(name=degree))

        for subject in subjects: 
            service.create_subject(schemas.Subject(name=subject, degree_id=degree_db.id))

    for student in students:
        service.insert_student_info(schemas.StudentInfoBase(**student))

    print("Data loaded successfully.")



create_data(degree_subjects, students)