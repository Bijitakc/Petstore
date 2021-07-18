from django.contrib import admin
from django.urls import path,include
from .views import index,petshop,petfood,pettoy,cart

urlpatterns = [
    path('',index,name='index'),
    path('petshop/',petshop.as_view(),name='petshop'),
    path('petfood/',petfood.as_view(),name='petfood'),
    path('pettoy/',pettoy.as_view(),name='pettoy'),
    path('mycart/',cart,name='cart')
]
