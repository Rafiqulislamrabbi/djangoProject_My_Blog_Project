FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt .
RUN pip install -r requirements.txt
