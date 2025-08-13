#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "PostgreSQL is up!"

echo "Running migrations..."
python manage.py migrate

echo "Starting server..."
exec "$@"
