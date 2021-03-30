from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def login(reques):
    return HttpResponse('Hello django world')
