FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./data_seeder.py /code/data_seeder.py

COPY ./app /code/app

COPY ./tests /code/tests

COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh

RUN chmod a+x docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]


