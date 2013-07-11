## Introduction

Tiny.cfil.es is an URL shortener written in Python using the Flask framework.
This is a fork of [Shorty](https://github.com/mattoufoutu/shorty).

## Dependencies

- Flask==0.8
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Script (only needed to run the application from the `manage.py` script)

## Running it

Install the required dependencies with `pip`

    pip install -r requirements.txt

Set up the database

    python manage.py syncdb

and then, to run it with the Flask's development server, use the `manage.py` script

    python manage.py runserver

To run the application in a production environment, refer to [Flask's documentation]
(http://flask.pocoo.org/docs/deploying/)
about deployment options.
