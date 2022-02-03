# Contacts Calendar

A page for contacts management with basic fields as first name, last name,
phone number, email and date of birth.
View in https://contacts-calendar.herokuapp.com/

## Installation

Steps for clone and recreate this page yourself.

### Installing

#### Python environment

Clone this project

```bash
git clone https://github.com/Patrick564/contacts_calendar.git
```

If you don't have a virtual environment create one (call folder as you like)

```bash
python -m venv .venv
```

And activate with the command

```bash
source .venv/bin/activate
```

Install the requirements

```bash
pip install -r requirements.txt
```

#### Django environment

First make the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

## Run server

Configure the environments variables in a .env file at the same level
what settings folder

Then run server

```bash
python manage.py runserver
```

## Build with

[Django](https://github.com/django/django) is used as the backend framework,
customizing the User base model, authentication URLs and login methods.

[Tailwind CSS](https://github.com/tailwindcss/tailwindcss) is used as CSS framework.
