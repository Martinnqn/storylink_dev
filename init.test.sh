#!/bin/sh
#python manage.py test
coverage run --source='.' manage.py test
#coverage report
#coverage xml -o ./coverage_report/coverage.xml
coverage xml
- bash <(curl -s https://codecov.io/bash)