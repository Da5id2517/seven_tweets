FROM python:3.6.1

RUN mkdir app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]