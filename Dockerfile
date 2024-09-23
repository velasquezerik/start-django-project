# Pull base image
FROM python:3.12

# set default environment variables
ENV PYTHONFAULTHANDLER=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  LANG=C.UTF-8

# Create user
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

# Install system dependencies
RUN apt-get update && apt-get install python3-dev gcc build-essential libpq-dev git -y

# Needed for SAML support
RUN  apt-get -y install libxml2-dev libxmlsec1-dev libxmlsec1-openssl

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Install project dependencies
COPY Pipfile /home/user/app/
COPY Pipfile.lock /home/user/app/
COPY Requirements.txt /home/user/app/

# Set work directory
WORKDIR /home/user/app/

# Install python dependencies
RUN pipenv install --dev --ignore-pipfile --system
RUN pip install -r Requirements.txt

# Create dynamic directories
RUN mkdir /home/user/app/logs
RUN mkdir /home/user/app/media

COPY . /home/user/app/

# Set work directory
WORKDIR /home/user/app/

USER user

EXPOSE 8000

# CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn conf.wsgi:application --log-file - -bind 0.0.0.0:8000 --reload