from django.contrib import admin
from django.urls import path,include
from .views import index,petshop,petfood,pettoy

urlpatterns = [
    path('',index,name='index'),
    path('petshop/',petshop,name='petshop'),
    path('petfood/',petfood,name='petfood'),
    path('pettoy/',pettoy,name='pettoy'),

]
