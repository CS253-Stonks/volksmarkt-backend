from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    is_buyer = models.BooleanField('buyer status', default=False)
    is_seller = models.BooleanField('seller status', default=False)
     
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255,default="NULL")
    
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255,default="NULL")
    