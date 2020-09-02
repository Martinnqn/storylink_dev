#!/bin/sh
#coverage xml -o /home/app/web/coverage_report/coverage.xml
echo "$CI"
if [ "$CI" ];
then
    echo "1"
    coverage run manage.py test apps/users/
    coverage report
    coverage xml
    mv coverage.xml /home/app/web/coverage_report/
else
    echo "2"
    python manage.py test
fi