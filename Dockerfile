# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /contacts_calendar/

COPY requirements.txt /contacts_calendar/

RUN pip install -r requirements.txt

COPY . /contacts_calendar/
