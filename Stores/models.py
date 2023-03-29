from django.db import models
from django.core.validators import MinLengthValidator
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

Categories = [('Electronics' , 'Electronics'),
              ('Medical' , 'Medical'),
              ('Stationary' , 'Stationary'),
              ('Print' , 'Print'),
              ('General Store' , 'General Store'),
              ('grocery', 'grocery'),
              ('books', 'books'),
              ('food' , 'food'),
              ('Others' , 'Others')]

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    category = models.CharField( choices=Categories , null=True , max_length=20 )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()    
    store = models.ForeignKey(Store , related_name="products" , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    
    def __str__(self):
        return self.name

