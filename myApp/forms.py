from django import forms
from .models import Guest
from django.contrib.auth.hashers import make_password


class GuestSignUpForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'password', 'mobile_number', 'gender', 'age']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Guest.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def save_guest(self):
        name = self.cleaned_data.get('name')
        if len(name) % 2 == 0:
            partition = 'even_partition'
        else:
            partition = 'odd_partition'

        password = make_password(self.cleaned_data.get('password'))
        
        guest = self.save(commit=False)
        guest.partition_key = partition
        guest.password = password
        guest.save()
