"""volksmarkt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('Cart/',views.CartList.as_view(), name='cart-list'),
    path('Cart/<int:pk>/',views.CartDetail.as_view(), name='cart-detail'),
    path('CartItem/',views.CartItemList.as_view(), name='cart-list'),
    path('CartItem/<int:pk>/',views.CartItemDetail.as_view(), name='cart-detail'),
]