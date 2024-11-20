#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # wait-for-it을 사용하여 db_first의 PostgreSQL이 준비될 때까지 대기
    /usr/local/bin/wait-for-it db_first:5432 -t 30

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec gunicorn config.wsgi:application --bind 0.0.0.0:8100