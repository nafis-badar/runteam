from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def name_wheel(request):
    return render(request, 'name_wheel.html')


def number_wheel(request):
    return render(request, 'number_wheel.html')
