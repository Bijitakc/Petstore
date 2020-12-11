from django.db import models
from django import forms

from django.contrib.auth.models import User

class UserModel(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.TextField()
    name=models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.auth.username
