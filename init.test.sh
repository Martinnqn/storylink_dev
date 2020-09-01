#!/bin/sh
#python manage.py test
coverage run manage.py test
echo 'terminaa'
#coverage report
coverage erase
echo 'borra'
chmod -R +rwx /home/app/web/coverage_report/
echo 'permisos'
#coverage xml -o /home/app/web/coverage_report/coverage.xml
coverage xml
ls
pwd
mv coverage.xml /home/app/web/coverage_report/
