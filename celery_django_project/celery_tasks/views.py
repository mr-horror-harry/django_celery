# from django.shortcuts import render
from .tasks import *
from django.http import HttpResponse

# Create your views here.
def test(request):
    add_data.delay(10.0, 2120)
    return HttpResponse("Successfully done task...")