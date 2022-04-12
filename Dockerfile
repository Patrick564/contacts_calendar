# @remind ToDo a dockerfile for database and web server

FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /contact_calendar

ADD . /contact_calendar/

RUN pip install -r requirements.txt
