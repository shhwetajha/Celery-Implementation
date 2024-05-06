from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_practice.settings')
app=Celery('celery_practice')
app.conf.enable_utc=False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

# CELERY BEAT SETTINGS

app.conf.beat_schedule={}
# load task modules from all registered Django apps.,it will go to each app and check is there any task
app.autodiscover_tasks()
#below written code is not mandot
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')