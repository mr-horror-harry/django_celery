from __future__ import absolute_import, unicode_literals
import os, json

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY_')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

def interval_periodic_tasks():
    from django_celery_beat.models import PeriodicTask, IntervalSchedule
    # executes every 10 seconds.
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Add Data interval',
        task='celery_tasks.tasks.add_data',
        args=json.dumps([123, 1230]),
    )

def crontab_periodic_tasks():
    from django_celery_beat.models import PeriodicTask, CrontabSchedule
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='59',
        hour='10',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Sub Data crontab',
        task='celery_tasks.tasks.sub_data',
        args=json.dumps([143, 1230]),
    )

# Delay execution until Django is ready
@app.on_after_configure.connect
def on_after_configure(sender, **kwargs):
    interval_periodic_tasks()
    crontab_periodic_tasks()
