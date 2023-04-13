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
        
from django.contrib.auth import authenticate
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user: # and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")