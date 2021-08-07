from django.contrib import admin
from django.urls import path,include
from .views import Index,Petshop,Petfood,Pettoy,Cart, blogdetail,blogview

urlpatterns = [
    path('',Index,name='index'),
    path('petshop/',Petshop.as_view(),name='petshop'),
    path('petfood/',Petfood.as_view(),name='petfood'),
    path('pettoy/',Pettoy.as_view(),name='pettoy'),
    path('blogs/', blogview , name='blog'),
    path('blogdetail/<int:id>', blogdetail, name ='blogdetail'),
    path('mycart/',Cart,name='cart')
]
