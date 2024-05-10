from django.shortcuts import render
from .tasks import test_func,send_email
from django.http import HttpResponse
from django.contrib.auth.models import User
from django_celery_beat.models import CrontabSchedule,PeriodicTask
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("done")


def test2(request):
    send_email.delay()
    return HttpResponse("sent")

def schedule_task(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=15,minute=15)
    task=PeriodicTask.objects.create(crontab=schedule,name='send_automated_mail_10',task='main.tasks.send_email')
    return HttpResponse("done")

# ,args=json.dumps(([[2,3]]))

