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

- **GET** `/students/` - Obtener las lista de los alumnos y sus materias inscriptas.
- **POST** `/students/` - Crea un nuevo estudiante y registra las materias que cursa.
- **GET** `/students/{student_id}` - Obtener detalles de un alumno específico.

Para ver una lista completa de rutas y sus especificaciones, puedes consultar la documentación automática generada por FastAPI en `http://localhost:80/docs`.



