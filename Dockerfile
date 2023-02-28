FROM python:3.10.10-buster

ENV PORT=$PORT
ENV DJANGO_SETTINGS_MODULE=contacts_calendar.settings.local

RUN mkdir -p /contacts_calendar

WORKDIR /contacts_calendar

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
COPY manage.py .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python manage.py collectstatic --no-input

EXPOSE $PORT

CMD python manage.py collectstatic --no-input && gunicorn --bind 0.0.0.0:$PORT contacts_calendar.wsgi
