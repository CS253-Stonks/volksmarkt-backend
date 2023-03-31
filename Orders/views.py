from django.http import HttpResponse
from django.shortcuts import render
from Orders.models import Cart, CartItem
from accounts.models import Buyer
from Orders.serializers import CartSerializer, CartItemSerializer
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# class CurrentBuyerCart(APIView):
#     def get(self, request, format=None):
#         user = request.user
#         if hasattr(user , 'cart'):
#             cart1 = user.cart
#             items = cart1.cartitem_set
#             serializer = CartItemSerializer(items, many=True)
#             return Response(serializer.data)
#         else:
#             return HttpResponse ("<html>login required</html>")
        
class CurrentBuyerCart(APIView):

    def get_object(self, pk):
        try:
            return Buyer.objects.get(pk=pk)
        except Buyer.DoesNotExist:
            raise Http404

    def get(self, request, pk , format=None):
        buyer = self.get_object(pk)
        cart1 = buyer.cart
        items = cart1.cart_items
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        buyer = self.get_object(pk)
        cart1 = buyer.cart
        data = request.data
        data.update({'cart':cart1.id})
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

   