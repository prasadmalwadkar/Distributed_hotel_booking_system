from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def all_user(request):
    return HttpResponse('returning all users')

def home(request) :  # request is an object that contains information
    return render(request, 'home.html')

def guestlogin(request):
    return render(request,'guestlogin.html')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        password = request.POST.get('password')
        username = full_name.split()[0]  # Simple way to create a username from the full name
        user = User.objects.create_user(username=username, password=password, first_name=full_name)
        user.save()
        login(request, user)  # Automatically log in the user
        return redirect('home')  # Redirect to the home page after signup
    return render(request, 'signup.html')