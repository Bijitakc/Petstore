from django.shortcuts import render,redirect

from .models import PetModel,PetFoodModel,PetToyModel,Cartitem,Blog
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.


def Index(request):
    return render(request,'shopapp\index.html')

class Petshop(View):

    def post(self,request):
       petpostid=request.POST.get('petpost')
       petpost=PetModel.objects.get(id=petpostid)
       User=request.user
       try:
           current=Cartitem.objects.filter(user=User)[0]
           pet=current.pets.all()
           if petpost not in pet :
               current.pets.add(petpost)
               current.save()
       except IndexError:
           ins=Cartitem.objects.create(user=User)
           ins.pets.add(petpost)
           ins.save()
       return redirect('petshop')

    def get(self,request):
        petposts=PetModel.objects.all().order_by('price')
        context={
        'petposts':petposts
        }
        return render(request,'shopapp\petshop.html',context)

class Petfood(View):
    def get(self,request):
        petfoodposts=PetFoodModel.objects.all().order_by('price')
        context={
        'petfoodposts':petfoodposts
        }
        return render(request,'shopapp\petfood.html',context)

    def post(self,request):
        petfoodid=request.POST.get('petfoodpost')
        petfoodpost=PetFoodModel.objects.get(id=petfoodid)
        User=request.user
        try:
            current=Cartitem.objects.filter(user=User)[0]
            petfood=current.petfoods.all()
            if petfoodpost not in petfood:
                current.petfoods.add(petfoodpost)
                current.save()
        except IndexError:
            ins=Cartitem.objects.create(user=User)
            ins.petfoods.add(petfoodpost)
            ins.save()
        return redirect('petfood')

class Pettoy(View):
    def get(self,request):
        pettoyposts=PetToyModel.objects.all().order_by('price')
        context={
        'pettoyposts':pettoyposts
        }
        return render(request,'shopapp\pettoy.html',context)

    def post(self,request):
        User=request.user
        pettoyid=request.POST.get('pettoypost')
        pettoypost=PetToyModel.objects.get(id=pettoyid)
        try:
            current=Cartitem.objects.get(user=User)
            pettoy=current.pettoys.all()
            if pettoypost not in pettoy:
                current.pettoys.add(pettoypost)
                current.save()
        except IndexError:
            ins=Cartitem.objects.create(user=User)
            ins.pettoys.add(pettoypost)
            ins.save()
        return redirect('pettoy')

def Cart(request):
    User=request.user
    items=[]
    product=Cartitem.objects.get(user=User)
    print(product)
    if product:
        try:
            pets=product.pets.all()
            for pet in pets:
                items.append(pet)
        except IndexError:
            pass
        try:
            petfoods=product.petfoods.all()
            for petfood in petfoods:
                items.append(petfood)
        except IndexError:
            pass
        try:
            pettoys=product.pettoys.all()
            for pettoy in pettoys:
                items.append(pettoy)
        except IndexError:
            pass
    context={
        'items':items
    }

    return render(request,'shopapp\cart.html',context)

# def Delpost(request):
#     id=get_object_or_404()
#     if request.method=="DELETE":
#         Cartitem.objects.filter(id=id).delete()  


# def blog(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs' : blogs
#     }
#     return render(request, 'shopapp\blogs.html')