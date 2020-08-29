from django.shortcuts import render
from django.http import HttpResponse

# Create your tests here.

def index(request):
    return render(request, 'shop/index.html')

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