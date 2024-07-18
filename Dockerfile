# docker run -d --name mycontainer -p 80:80 myimage
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./create_example_data.py /code/create_example_data.py

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
VOLUME [ "/code/app" ]
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
#CMD ["fastapi", "dev", "app/main.py", "--port", "80"]


