FROM python:3.8

# settup a work directory

WORKDIR /usr/src/app

# enviroment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app