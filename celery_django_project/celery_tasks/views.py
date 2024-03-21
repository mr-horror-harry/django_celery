# from django.shortcuts import render
from .tasks import *
from django.http import HttpResponse

# Create your views here.
def add_req(request):
    add_data.delay(10.0, 2120)
    return HttpResponse("Successfully done add task...")

def sub_req(request):
    sub_data.delay(1054.0, 2230)
    return HttpResponse("Successfully done sub task...")

def mul_req(request):
    mul_data.delay(10.0, 21)
    return HttpResponse("Successfully done mul task...")
