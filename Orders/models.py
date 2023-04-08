from django.db import models
from Stores.models import Store, Product
from accounts.models import Buyer

# Create your models here.
    
# class Cart(models.Model):
#     buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE , related_name="cart")

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE , related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return self.product

class Order(models.Model):
    # refcode = models.CharField(max_length=20)
    buyer = models.ForeignKey(Buyer , on_delete=models.CASCADE , related_name="orders")
    total_cost = models.PositiveIntegerField(default=0)
    deliveryaddress = models.TextField()
    order_date = models.DateField(auto_now_add=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)

