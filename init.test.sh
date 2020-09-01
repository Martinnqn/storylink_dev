#!/bin/sh
#python manage.py test
coverage run --source='.' manage.py test
coverage report