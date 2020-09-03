from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('trackker/', views.trackker, name="trackker"),
    path('search/', views.search, name="search"),
    path('products/<int:myid>', views.productview, name="productview"),
    path('checkout/', views.checkout, name="checkout"),
]
