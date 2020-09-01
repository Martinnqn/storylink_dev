#!/bin/sh
#python manage.py test
coverage run manage.py test apps/users/
echo 'crea'
coverage report
chmod -R +rwx /home/app/web/coverage_report/
#coverage xml -o /home/app/web/coverage_report/coverage.xml
coverage xml
ls
pwd
mv coverage.xml /home/app/web/coverage_report/
