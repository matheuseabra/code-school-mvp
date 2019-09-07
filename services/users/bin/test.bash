#!/usr/bin/env bash

echo "Running tests..."

cd ../../.. 

docker-compose -f docker-compose-prod.yml exec users python manage.py test