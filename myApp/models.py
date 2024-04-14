from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager 
from datetime import datetime


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    partition_key = models.CharField(max_length=64, editable=False)

    class Meta:
        # Define the database table name
        db_table = 'guest'

    def save(self, *args, **kwargs):
        # Calculate the length of the name
        name_length = len(self.name)
        
        # Determine if the length is odd or even
        is_odd_length = name_length % 2 != 0

        # Set the partition key based on whether the length is odd or even
        if is_odd_length:
            self.partition_key = 'odd_partition'
        else:
            self.partition_key = 'even_partition'
        
        super(Guest, self).save(*args, **kwargs)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    guest_id = models.IntegerField()
    room_id = models.IntegerField()
    room_type = models.CharField(max_length=50)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booking_status = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_partition(cls, room_type, checkin_date):
        room_partition = 'deluxe' if room_type.lower() == 'deluxe' else 'standard'
        month_partition = checkin_date.month
        return f"p_{room_partition}_{month_partition:02d}"
