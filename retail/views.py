from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "retail/index.html")


def contact(request):
    return render(request, "retail/contact.html")


def about(request):
    return render(request, "retail/about.html")


def cart(request):
    return render(request, "retail/cart.html")


def checkout(request):
    return render(request, "retail/checkout.html")


def product_details(request):
    return render(request, "retail/product-details.html")


def wishlist(request):
    return render(request, "retail/wishlist.html")
