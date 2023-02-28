FROM python:3.10.10-buster

ENV PORT=$PORT
ENV DJANGO_SETTINGS_MODULE=contacts_calendar.settings.local
ENV APP=/contacts_calendar

RUN mkdir -p $APP

WORKDIR $APP

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $APP

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD python manage.py collectstatic && python manage.py makemigrations && python manage.py migrate && gunicorn --bind $PORT --workers 1 contacts_calendar.wsgi
