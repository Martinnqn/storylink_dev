#!/bin/sh
#python manage.py test
coverage run manage.py test
echo 'terminaa'
#coverage report
coverage erase
echo 'borra'
coverage xml -o /home/app/web/coverage_report/coverage.xml
