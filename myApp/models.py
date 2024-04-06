from django.db import models
from django.contrib.auth.models import User 

class Contact(models.Model):
    id=models.AutoField(primary_key=True)   
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
    def __str__(self):
        return "{}".format(self.name) 

# Create your models here.
