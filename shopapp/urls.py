from django.contrib import admin
from django.urls import path,include
from .views import Index,Petshop,Petfood,Pettoy,Cart

urlpatterns = [
    path('',Index,name='index'),
    path('petshop/',Petshop.as_view(),name='petshop'),
    path('petfood/',Petfood.as_view(),name='petfood'),
    path('pettoy/',Pettoy.as_view(),name='pettoy'),
    # path('blogs/', theblogs , name='theblogs'),
    path('mycart/',Cart,name='cart')
]
