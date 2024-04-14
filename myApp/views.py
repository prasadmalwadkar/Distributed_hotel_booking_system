from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import messages
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.timezone import now
from .models import Booking
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GuestUserForm, GuestForm
from django.contrib.auth.hashers import make_password
from myApp.models import Guest
# Create your views here.

def guestsignup_view(request):
    if request.method == 'POST':
        user_form = GuestUserForm(request.POST)
        guest_form = GuestForm(request.POST)
        
        if user_form.is_valid() and guest_form.is_valid():
            user = user_form.save()

            # Save guest data
            guest_data = guest_form.cleaned_data
            guest = Guest.objects.create(user=user, **guest_data)

            # Add user to guest group
            my_guest_group, _ = Group.objects.get_or_create(name='guest')
            my_guest_group.user_set.add(user)
            
            return HttpResponseRedirect('guestlogin')
    else:
        user_form = GuestUserForm()
        guest_form = GuestForm()

    context = {'user_form': user_form, 'guest_form': guest_form}
    return render(request, 'guestsignup.html', context)

def home(request) :  # request is an object that contains information
    return render(request, 'home.html')

def is_guest(user):
    return user.groups.filter(name='GUEST').exists()

def afterlogin_view(request):
    if is_guest(request.user):
        return redirect('guest-dashboard')

#def guestsignup(request):
#    if request.method == 'POST':
#        form = GuestSignUpForm(request.POST)
#        if form.is_valid():
#            form.save_guest()
#            return redirect('home')
#    else:
#        form = GuestSignUpForm()
#    
#    return render(request, 'guestsignup.html', {'form': form})




@login_required(login_url='guestlogin')
@user_passes_test(is_guest)
def guest_dashboard_view(request):
    guest_id = request.user.id  
    current_bookings = Booking.objects.filter(guest_id=guest_id, checkin_date__gte=now())
    past_bookings = Booking.objects.filter(guest_id=guest_id, checkout_date__lt=now())
    context = {
        'current_bookings': current_bookings,
        'past_bookings': past_bookings
    }
    return render(request, 'guest_dashboard.html', context)