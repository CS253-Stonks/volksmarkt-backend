from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import re_path
urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('buyer/login/',views.buyer_login,name='buyer_login'),
     path('buyer/register/',views.buyer_register,name='buyer_register'),
     re_path(r'^api/v1/', include('djoser.urls')),
     re_path(r'^api/v1/', include('djoser.urls.authtoken')),
]