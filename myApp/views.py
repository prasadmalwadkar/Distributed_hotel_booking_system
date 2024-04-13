from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import GuestSignUpForm
# Create your views here.

def all_user(request):
    return HttpResponse('returning all users')

def home(request) :  # request is an object that contains information
    return render(request, 'home.html')

def guestlogin(request):
    return render(request,'guestlogin.html')



def guestsignup(request):
    if request.method == 'POST':
        form = GuestSignUpForm(request.POST)
        if form.is_valid():
            form.save_guest()
            return redirect('home')
    else:
        form = GuestSignUpForm()
    
    return render(request, 'guestsignup.html', {'form': form})