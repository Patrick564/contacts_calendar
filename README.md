# Contacts Calendar

A page for contacts management with basic fields as first name, last name,
phone number, email and date of birth.
[View in here](https://contacts-calendar.onrender.com)

Example email: example@contacts.com and Password: RenderDeploy12345

![screenshot1](https://raw.githubusercontent.com/Patrick564/static-files/main/screenshots/contact-1.png)
![screenshot2](https://raw.githubusercontent.com/Patrick564/static-files/main/screenshots/contact-2.png)

## Installation

Steps for clone and recreate this page yourself using Python3.9.7 and Poetry.
Also can use the [docker image](https://hub.docker.com/repository/docker/patrick794/contacts-calendar) with docker-compose file

### Installing

#### Python environment

Clone this project

```bash
git clone https://github.com/Patrick564/contacts_calendar.git
```

Create the virtualenv with Poetry and install dependences.

```bash
poetry env use python3.9.7
poetry shell
poetry install
```

And put your env vars in a .env file, like example.env.

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
