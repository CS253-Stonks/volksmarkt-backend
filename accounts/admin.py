from django.contrib import admin
from .models import Buyer, Seller, User
# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(User)