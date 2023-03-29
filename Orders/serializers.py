from rest_framework import serializers
from Stores.models import Store, Product
from Orders.models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    cartitem_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    class Meta:
        model = Cart
        fields = ['id', 'buyer', 'cartitem_set']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart' , 'quantity' ]

