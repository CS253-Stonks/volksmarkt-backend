from django.db import models
from django.contrib.auth.models import User
     
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255,default="NULL")

    def __str__(self):
        return self.user.username
    
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255,default="NULL")

    def __str__(self):
        return self.user.username
    