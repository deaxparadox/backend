FROM python:latest
ENV PYTHONUNBUFFERED 1
# RUN apt-get update && apt-get install build-essential -y
WORKDIR /django/
COPY . .
EXPOSE 8000
RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN python manage.py runserver

