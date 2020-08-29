from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your tests here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    params = {'nSlide': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)

def aboutus(request):
    return render(request, 'shop/about.html')

def contactus(request):
    return HttpResponse("We are at contact")    

def trackker(request):
    return HttpResponse("We are at trackker")

def productview(request):
    return HttpResponse("We are at productView")    

def search(request):
    return HttpResponse("We are at search")

def checkout(request):
    return HttpResponse("We are at checkout")