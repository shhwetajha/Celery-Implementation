from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("done")
