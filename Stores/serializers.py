from rest_framework import serializers
from Stores.models import Store, LANGUAGE_CHOICES, STYLE_CHOICES, Product


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'contact','products']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']
