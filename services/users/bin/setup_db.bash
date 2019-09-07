#!/usr/bin/env bash

echo "Setting up database config and seeds"

cd ../../..

docker-compose -f docker-compose-prod.yml exec users python manage.py recreate_db

docker-compose -f docker-compose-prod.yml exec users python manage.py seed_db