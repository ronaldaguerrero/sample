### first app, def functions here ###
from django.shortcuts import render, HttpResponse, redirect
from .models import * 
def index(request):
    return render(request, 'first_app/index.html')

def zo(request):
    return render(request, 'first_app/zo.html')

def shaq(request):
    return render(request, 'first_app/shaq.html')

def cart(request):
    return render(request, 'first_app/cart.html')

def orders(request):
    return render(request, 'first_app/orders.html')

def products(request):
    return render(request, 'first_app/products.html')

def order(request):
    return render(request, 'first_app/order.html')