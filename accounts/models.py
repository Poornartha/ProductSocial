from django.db import models
from django.contrib import auth

# Create your models here.
# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return '{}'.format(self.username)

default_gender = "male"

class Customer(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    favourite_color = models.CharField(max_length=100)
    favourite_item = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, default=default_gender)
