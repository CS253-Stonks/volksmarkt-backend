from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Buyer

class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

@csrf_exempt
def buyer_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user:
        msg = {
            'isAuthenticated':True,
            'user':user.get_username()
        }
    else:
        msg = {
            'isAuthenticated':False
        }
    return JsonResponse(msg)

@csrf_exempt
def buyer_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    address = request.POST.get('address')
    username = str(email).split('@')[0]
    try:
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email = email,
            username = username,
            password = password
        )
        buyer = Buyer.objects.create(
            user = user,
            address = address
        )
        msg = {
            'isCreated':True,
            'buyerId': buyer.pk
        }
    except Exception as exception :
        msg = {
            'isCreated':False,
            'msg':f"Failed to create Buyer due to ${exception}"
        }
    return JsonResponse(msg)