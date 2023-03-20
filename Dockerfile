FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY . /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080
ENV PORT 8080
ENV HOST 0.0.0.0

CMD ["python3" , "main.py"]
