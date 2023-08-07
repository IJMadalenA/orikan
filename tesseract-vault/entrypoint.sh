#!/bin/sh

if [ "$DATABASE" = "solemnace_galleries" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

# VERIFY IF THERE ARE NO MIGRATIONS TO CREATE, AND IF THERE ARE, MAKE THE MIGRATIONS.
# https://docs.djangoproject.com/en/4.1/ref/django-admin/#django-admin-makemigrations
python manage.py makemigrations --no-input --merge

# TRY TO APPLY THE MIGRATIONS UNTIL THE DATABASE IS READY.
until python manage.py migrate --no-input || exit 1
do
    echo "MIGRATE: Waiting for db to be ready..."
    sleep 2
done

# COLLECT THE STATIC FILES.
# https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/
python manage.py collectstatic --no-input --clear

exec "$@"
