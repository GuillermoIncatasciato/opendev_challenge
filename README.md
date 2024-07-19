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
    docker compose up
    ```

    Este comando construirá las imágenes necesarias y levantará los contenedores definidos en el archivo `docker-compose.yml`.

3. **Agregar datos de prueba (Opcional)**

    Una vez que los contenedores estén corriendo, agrega datos de prueba ejecutando el siguiente comando:

    ```bash
    docker exec -it opendev_challenge-mycontainer python data_seeder.py
    ```

    Asegúrate de que el nombre del contenedor (`opendev_challenge-mycontainer`) coincida con el del contenedor en ejecución.

## Uso

Una vez que los contenedores estén corriendo, la API estará disponible en `http://localhost:80`.

### Rutas de la API

- **GET** `/students/` - Obtener la lista de los alumnos y sus materias inscriptas.
- **POST** `/students/` - Crea un nuevo estudiante y registra las materias que cursa.
- **GET** `/students/{student_id}` - Obtener detalles de un alumno específico.

Para ver una lista completa de rutas y sus especificaciones, puedes consultar la documentación automática generada por FastAPI en `http://localhost:80/docs`.

## Ejemplos de Solicitud con `curl`

    Para obtener una lista de estudiantes desde el endpoint `/students` con paginación, puedes usar el siguiente comando:

    ```bash
    curl -X 'GET' \
    'http://localhost/students/?skip=2&limit=6' \
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

    (Nota: los ids de materias validos despues del correr data_seeder.py son del 1 al 15).
    - La request no sera valida si los subjects_id se repiten en el campo sujects.
    - El estudiante no se cargara si el email ya ha sido registrado.
    - Se verificará que los ids de las materias sean validos (esten cargados en la base de datos).


