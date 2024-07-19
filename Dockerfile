FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./data_seeder.py /code/data_seeder.py

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

