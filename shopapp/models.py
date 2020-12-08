from django.db import models

# Create your models here.
class PetModel(models.Model):
    name=models.CharField(max_length=200)
    pet_image=models.ImageField(upload_to='img')
    price=models.TextField()

    class Meta:
        verbose_name_plural='petposts'

    def __str__(self):
        return self.name
class PetFoodModel(models.Model):
    foodname=models.CharField(max_length=200)
    food_image=models.ImageField(upload_to='img')
    food_price=models.TextField()

    class Meta:
        verbose_name_plural='petfoodposts'

    def __str__(self):
        return self.foodname

class PetToyModel(models.Model):
    toyname=models.CharField(max_length=200)
    toy_image=models.ImageField(upload_to='img')
    toy_price=models.TextField()

    class Meta:
        verbose_name_plural='pettoyposts'

    def __str__(self):
        return self.toyname





