from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_buyer = models.BooleanField('buyer status', default=False)
    is_seller = models.BooleanField('seller status', default=False)
    
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_id = models.CharField(max_length=50)   
