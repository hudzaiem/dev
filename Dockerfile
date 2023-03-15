FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY . /usr/src/app

COPY requirements.txt requirements.txt

RUN apt-get update & apt-get install -y git

RUN pip install -r requirements.txt

CMD ['python3' , 'main.py']