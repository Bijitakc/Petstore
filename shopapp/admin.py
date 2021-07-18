from django.contrib import admin
from .models import PetModel,PetFoodModel,PetToyModel,Profile,Cartitem

# Register your models here.
admin.site.register(PetModel)
admin.site.register(PetFoodModel)
admin.site.register(PetToyModel)
admin.site.register(Profile)
admin.site.register(Cartitem)
