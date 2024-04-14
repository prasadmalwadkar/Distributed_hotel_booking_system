from django import forms
from .models import Guest
from . import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Guest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


#class GuestSignUpForm(forms.ModelForm):
#    class Meta:
#        model = Guest
#        fields = ['name', 'email', 'password', 'mobile_number', 'gender', 'age']
#
#    def clean_email(self):
#        email = self.cleaned_data.get('email')
#        if Guest.objects.filter(email=email).exists():
#            raise forms.ValidationError('This email is already in use.')
#        return email
#
#    def save_guest(self):
#        name = self.cleaned_data.get('name')
#        if len(name) % 2 == 0:
#            partition = 'even_partition'
#        else:
#            partition = 'odd_partition'
#
#        password = make_password(self.cleaned_data.get('password'))
#        
#        guest = self.save(commit=False)
#        guest.partition_key = partition
#        guest.password = password
#        guest.save()


class GuestUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Sign Up'))

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'password', 'mobile_number', 'gender', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Sign Up'))
