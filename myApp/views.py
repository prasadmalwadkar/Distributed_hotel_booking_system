from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_user(request):
    return HttpResponse('returning all users')

def home(request) :  # request is an object that contains information
    return render(request, 'home.html')