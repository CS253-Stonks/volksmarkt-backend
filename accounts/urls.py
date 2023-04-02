from django.urls import path
from . import views
urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('buyer/login/',views.buyer_login,name='buyer_login'),
     path('buyer/register/',views.buyer_register,name='buyer_register'),
]