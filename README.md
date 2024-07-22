# FastAPI REST API

Este es un proyecto de API REST construido con [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/) y [PostgreSQL](https://www.postgresql.org/).

## Prerequisitos

- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) deben estar instalados en tu sistema.

## Instalación

1. **Clona el repositorio**

    ```bash
    git clone https://github.com/GuillermoIncatasciato/opendev_challenge.git
    cd opendev_challenge
    ```

2. **Construye y corre los contenedores**

    ```bash
    export POSTGRES_PASSWORD=TestPassword4321
    docker compose up
    ```

    Este comando construirá las imágenes necesarias y levantará los contenedores definidos en el archivo `docker-compose.yml`.

3. **Agregar datos de prueba**

    Una vez que los contenedores estén corriendo, agrega datos de prueba ejecutando el siguiente comando:

    ```bash
    docker compose exec -it backend python data_seeder.py
    ```

## Uso

Una vez que los contenedores estén corriendo, la API estará disponible en `http://localhost:80`.

### Rutas de la API

- **POST** `/students/` - Crea un nuevo estudiante y registra las materias que cursa.

  **Descripción de los campos del Body:**

  - `name`: *string* - Nombre completo.
  - `email`: *string* - Correo electrónico.
  - `address`: *string* - Dirección.
  - `phone`: *integer* - Número de teléfono.
  - `subjects`: *array* - Lista de materias que el estudiante está cursando.
    - `subject_id`: *integer* - Id de la materia.
    - `enrollment_year`: *integer* - Año en el que el estudiante se inscribió en la materia.
    - `times_taken`: *integer* - Número de veces que el estudiante ha cursado la materia.


- **GET** `/students/` - Obtener la lista de los alumnos y sus materias inscriptas.
- **GET** `/students/{student_id}` - Obtener detalles de un alumno específico.
- **GET** `/subjects/` - Obtener la lista completa de materias.
- **GET** `/degrees/` - Obtener la lista de carreras.
- **GET** `/degrees/{degree_id}/subjects` - Obtener la lista de materias de la carrera con id `degree_id`.

Para ver una lista completa de rutas y sus especificaciones, puedes consultar la documentación automática generada por FastAPI en [http://localhost:80/docs](http://localhost:80/docs).


## Ejemplos de solicitudes con `curl`

Para obtener una lista de estudiantes desde el endpoint `/students` con paginación, puedes usar el siguiente comando:

```bash
curl -X 'GET' \
'http://localhost/students/?skip=5&limit=10' \
-H 'accept: application/json'
```
Para obtener la información de un único estudiante desde el endpoint `/students`:

```bash
curl -X 'GET' \
'http://localhost/students/3' \
-H 'accept: application/json'
```
Para cargar la información de un nuevo estudiante desde el endpoint `/students`:

```bash
curl -X 'POST' \
'http://localhost/students/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
        "name": "Francisco López",
        "email": "francisco.lopez@example.com",
        "address": "Ruta Nacional 101, Campo",
        "phone": 123456789,
        "subjects": [
            {"subject_id": 4, "enrollment_year": 2020, "times_taken": 2},
            {"subject_id": 8, "enrollment_year": 2019, "times_taken": 1},
            {"subject_id": 13, "enrollment_year": 2021, "times_taken": 3}
        ]
    }'
```

**Notas importantes para la carga de un estudiante:**

- La solicitud será inválida si alguno de los `subject_id` proporcionados en el cuerpo de la solicitud no existe en la base de datos.
- El estudiante no será registrado si el correo electrónico (`email`) ya está asociado a otro estudiante en la base de datos.
- Todos los `subject_id` en el cuerpo de la solicitud deben ser diferentes.
