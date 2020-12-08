from django.contrib import admin
from .models import PetModel,PetFoodModel,PetToyModel

# Register your models here.
admin.site.register(PetModel)
admin.site.register(PetFoodModel)
admin.site.register(PetToyModel)
