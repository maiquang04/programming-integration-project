from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "retail/index.html")


def contact(request):
    return render(request, "retail/contact.html")


def about(request):
    return render(request, "retail/about.html")
