from django.shortcuts import render

from .models import PetModel,PetFoodModel,PetToyModel

# Create your views here.
def index(request):
    return render(request,'shopapp\index.html')

def petshop(request):
    petposts=PetModel.objects.all().order_by('name')
    context={
        'petposts':petposts
    }
    return render(request,'shopapp\petshop.html',context)

def petfood(request):
    petfoodposts=PetFoodModel.objects.all().order_by('foodname')
    context={
        'petfoodposts':petfoodposts
    }
    return render(request,'shopapp\petfood.html',context)

def pettoy(request):
    pettoyposts=PetToyModel.objects.all().order_by('toyname')
    context={
        'pettoyposts':pettoyposts
    }
    return render(request,'shopapp\pettoy.html',context)