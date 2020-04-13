from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
#/products -> index
# uniform resource Locator(Address)
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products' : products})



def new(reques):
    return HttpResponse('New Prodcut')





