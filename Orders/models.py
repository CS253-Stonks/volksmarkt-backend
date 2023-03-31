from django.db import models
from Stores.models import Store, Product
from accounts.models import Buyer

# Create your models here.
    
class Cart(models.Model):
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE , related_name="cart")

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

# class Order(models.Model):
#     refcode = models.CharField(max_length=20)
#     deliveryaddress = models.TextField()
#     order_date = models.DateField(auto_now_add=True)
#     cart = models.OneToOneField(Cart)
