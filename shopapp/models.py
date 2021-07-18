from django.db import models
from django.contrib.auth import get_user_model
import datetime

User=get_user_model()

# Create your models here.

class PetModel(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img')
    price=models.TextField()
    value=models.TextField(default="pet")

    class Meta:
        verbose_name_plural='petposts'

    def __str__(self):
        return self.name
class PetFoodModel(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img')
    price=models.TextField()
    value=models.TextField(default="petfood")

    class Meta:
        verbose_name_plural='petfoodposts'

    def __str__(self):
        return self.name

class PetToyModel(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img')
    price=models.TextField()
    value=models.TextField(default="pettoy")

    class Meta:
        verbose_name_plural='pettoyposts'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pets=models.ManyToManyField(PetModel,blank=True)
    petfoods=models.ManyToManyField(PetFoodModel,blank=True)
    pettoys=models.ManyToManyField(PetToyModel,blank=True)

    class Meta:
        verbose_name_plural='profiles'


class Cartitem(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    pets=models.ManyToManyField(PetModel,blank=True)
    petfoods=models.ManyToManyField(PetFoodModel,blank=True)
    pettoys=models.ManyToManyField(PetToyModel,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name="cart"
        verbose_name_plural="carts"

