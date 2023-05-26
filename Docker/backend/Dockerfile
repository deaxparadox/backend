FROM python:3.10-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update
# RUN apt-get install redis redis-server -y
# RUN /etc/init.d/redis-server start

# Copy project
COPY . .