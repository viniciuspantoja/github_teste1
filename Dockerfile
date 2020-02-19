# Getting base image
FROM python:3.7 AS base

MAINTAINER vinicius pantoja <vinicius.pantoja@gmail.com>

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .

RUN pip3 install pipenv
CMD pipenv install --deploy --ignore-pipfile --dev
