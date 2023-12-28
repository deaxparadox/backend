FROM python:3.12.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements_django_2.txt .
RUN pip install -r requirements_django_2.txt

# copy project
COPY . .


ENTRYPOINT [ "sh", "run.sh" ]