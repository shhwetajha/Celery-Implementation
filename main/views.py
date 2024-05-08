from django.shortcuts import render
from .tasks import test_func,send_email
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("done")


def test2(request):
    send_email.delay()
    return HttpResponse("sent")
