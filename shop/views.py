from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your tests here.

def index(request):
    # products = Product.objects.all()
    # print(products.0.product_desc)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params = {'nSlide': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # The above line forms a list of related categories
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        # Below we are making list of lists.
        # Each list has a particular category of product in it
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
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