# kind of base on https://runnable.com/docker/python/dockerize-your-flask-application
FROM python:3.8-buster

RUN apt update && apt-get -y install nano

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
