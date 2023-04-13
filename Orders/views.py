from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Orders.models import CartItem, Order, OrderItem
from accounts.models import Buyer
from Orders.serializers import CartItemSerializer, OrderMiniSerializer, OrderFullSerializer, OrderItemSerializer
from rest_framework import generics
from django.core.mail import send_mail
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# class CartList(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class CartDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

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
        items = buyer.cart_items
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        buyer = self.get_object(pk)
        data = request.data
        data.update({'buyer':buyer.pk})
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PlaceOrder(APIView):        
    def post(self, request, pk, format=None):
        buyer = get_object_or_404(Buyer , pk=pk)
        # cartitems = buyer.cart_items
        data = request.data
        data.update({'buyer':pk})
        serializer = OrderMiniSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            order = Order.objects.get(id=serializer.data['id'])
            for item in buyer.cart_items.all():                
                OrderItem.objects.create(product=item.product , order=order , quantity=item.quantity)
                item.delete()
            serializer = OrderMiniSerializer(order)
            email_body = "Your order details are: " + serializer.data;
            email = buyer.email
            send_mail(
            "Welcome to Volksmarkt",
            email_body,
            "volksmarkt.iitk@gmail.com",
            [email],
            fail_silently=False,)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    def get(self, request, pk , format=None):
        buyer = get_object_or_404(Buyer , pk=pk)
        orders = buyer.orders
        serializer = OrderMiniSerializer(orders, many=True)
        return Response(serializer.data)
    

class OrderDetail(APIView):
    def get(self, request, pk , format=None):
        order = get_object_or_404(Order , pk=pk)
        serializer = OrderFullSerializer(order)
        return Response(serializer.data)
    

class OrderItemDetail(APIView):
    def get(self, request, pk , format=None):
        item = get_object_or_404(OrderItem , pk=pk)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)