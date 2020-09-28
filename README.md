# yatube
Социальная сеть блогеров

## installation
python -m venv .venv
venv\Scripts\activate
pip install -r requirements.txt

## django
django-admin startproject prj_name
python manage.py runserver

### app
python manage.py startapp blogapp
    other

## shell
python manage.py shell

## sql
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate blog 0001

## Testing
python manage.py test

python manage.py shell
    from django.test import Client

    client = Client()
    client.get()