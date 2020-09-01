#!/bin/sh
#python manage.py test
coverage run --source='.' manage.py test
#coverage report
cd coverage_report
ls
cd ..
sudo coverage xml -o ./coverage_report/coverage.xml