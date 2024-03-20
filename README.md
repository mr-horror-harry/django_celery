# requirements
python3, pip3

# venv setup
python3 -m venv venv

# required packages
pip install django

pip install celery

pip install redis

pip install django-celery-results

# named worker
celery -A django_celery.celery worker -n worker1 -l INFO

# integrated celery beat postgres
celery -A django_celery.beat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler