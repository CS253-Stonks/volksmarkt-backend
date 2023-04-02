from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'address']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'address']
