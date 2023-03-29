from django.db import models
from django.core.validators import MinLengthValidator
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.

    
# class Order(models.Model):
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     refcode = models.CharField(max_length=20)
#     deliveryaddress = models.TextField()
    
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    




