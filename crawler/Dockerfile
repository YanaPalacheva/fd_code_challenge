FROM python:3.8-slim

WORKDIR usr/src/crawler

# install dependencies for psycopg2 - PostgreSQL adapter for Python
RUN apt-get update
RUN apt-get -y install libpq-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "./crawler.py"]

