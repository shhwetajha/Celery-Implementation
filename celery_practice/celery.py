from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_practice.settings')
app=Celery('celery_practice')
app.conf.enable_utc=False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

# CELERY BEAT SETTINGS

app.conf.beat_schedule={
    'send_mail_everyday_at_8':{
        'task':'main.tasks.send_email',
        'schedule':crontab(hour=14,minute=52),
        # day_of_month=19,month_of_year=6 <= we can define thwse things also in schedule
    }
}
# load task modules from all registered Django apps.,it will go to each app and check is there any task
app.autodiscover_tasks()
#below written code is not mandot
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')