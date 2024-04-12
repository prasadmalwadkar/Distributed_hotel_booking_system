from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager 

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
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin