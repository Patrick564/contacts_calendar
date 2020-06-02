# Contacts Calendar

A page for contacts management with basic fields as first name, last name,
phone number, email and date of birth.

## Installation

Steps for clone and recreate this page yourself.

### Installing

Clone this proyect

```bash
git clone https://github.com/Patrick564/contacts_calendar.git
```

And install the file 'requirements.txt'

```bash
pip install -r requirements.txt
```

For Tailwind installation run, the folder name is 'theme', but you can name it
as you like, just make sure to change it in INSTALLED_APPS of settings.py

```bash
python manage.py tailwind init theme
python manage.py tailwind install
```

### Test

Use the Django tests

```bash
python manage.py test
```

## Build with

[Django](https://github.com/django/django) is used as the backend framework,
customizing the User base model, authentication URLs and login methods.

[Tailwind CSS](https://github.com/tailwindcss/tailwindcss) is used as CSS framework.

[Django-Tailwind](https://pypi.org/project/django-tailwind/) - for use Tailwind with Django.
