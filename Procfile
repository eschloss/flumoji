web: bin/start-pgbouncer-stunnel newrelic-admin run-program gunicorn openpds.wsgi --preload --max-requests 150 --worker-class gevent
worker: newrelic-admin run-program python manage.py celery worker -B -l info
