from django.shortcuts import render
from django.urls import path, include
from . import views

# Create your views here.
def home(request):
    return HttpResponse("hello")