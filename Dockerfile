FROM python:3.10.10-buster

ENV PORT=$PORT
ENV DJANGO_SETTINGS_MODULE=contacts_calendar.settings.local

RUN mkdir -p /contacts_calendar

WORKDIR /contacts_calendar

ENV PYTHONDOWNWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt && python manage.py collectstatic --no-input

COPY . .

EXPOSE $PORT

CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind $PORT --workers 1 contacts_calendar.wsgi
