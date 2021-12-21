from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from custom_User.managers import UserManager

# create the models' classes here

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    # add more fields.

    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default='False')
    is_superuser = models.BooleanField(default='False')
    is_active = models.BooleanField(default='True')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.email
