#!/bin/sh
set -e

if [ "$1" = 'gunicorn' ]; then
    shift
    exec gunicorn wsgi --name=api --bind=0.0.0.0:5000 --timeout=1800 "$@"
fi

exec "$@"
