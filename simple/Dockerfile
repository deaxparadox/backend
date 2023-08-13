FROM python:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -u 1000 -ms /bin/bash simple && mkdir /django && chown -R simple:simple /django
USER simple
# RUN apt-get update && apt-get install build-essential -y
WORKDIR /django
COPY --chown=simple:simple . .


EXPOSE 8000
RUN pip install --upgrade pip && pip install -r requirements.txt
# CMD [ "python", "manage.py", "runserver" ]

