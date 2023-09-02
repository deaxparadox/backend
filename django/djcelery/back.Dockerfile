# pull official base image
FROM python:3.11

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    # libpq-dev \
    # libmariadbclient-dev \
    # libjpeg62-turbo-dev \
    # zlib1g-dev \
    # libwebp-dev \
    adduser \
 && rm -rf /var/lib/apt/lists/*

RUN PATH="$PATH:/home/fire/.local/bin"


# Add use that will used in the container
RUN adduser fire

# Create a directory for setting up application
RUN mkdir /home/fire/backend -p
# RUN chown fire:fire backend

# set work directory
WORKDIR /home/fire/backend


USER fire

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy every to workdir
COPY --chown=fire:fire  . .


# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# run entrypoint.sh
ENTRYPOINT ["/home/fire/backend/entrypoint.sh"]
