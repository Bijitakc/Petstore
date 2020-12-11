from django.urls import path
from django.contrib import admin

from .views import loginview,registerview,logoutview,profile

urlpatterns = [
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logoutregister/', logoutview, name='logout'),
    path('profile/',profile, name='profile')
   
]