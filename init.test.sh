#!/bin/sh
#coverage xml -o /home/app/web/coverage_report/coverage.xml
if [ "$CI" ];
then
    coverage run manage.py test apps/users/
    coverage report
    coverage xml
    mv coverage.xml /home/app/web/coverage_report/
else
    python manage.py test
fi