from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Category, Product


# Create your views here.
def index(request):
    categories = Category.objects.all()

    best_selling_products = Product.objects.all().order_by("-sold_quantity")[:4]

    products = Product.objects.all()

    context = {
        "categories": categories,
        "best_selling_products": best_selling_products,
        "products": products,
    }

    return render(request, "retail/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "peer/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "retail/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request,
                "peer/sign-up.html",
                {"message": "Passwords must match."},
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "retail/sign-up.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "retail/sign-up.html")


def contact(request):
    return render(request, "retail/contact.html")


def about(request):
    return render(request, "retail/about.html")


def cart(request):
    return render(request, "retail/cart.html")


def checkout(request):
    return render(request, "retail/checkout.html")


def product_details(request):
    product_name = "Laptop Gaming Lenovo Legion 9 16IRX8 83AG0047VN"
    product_price = "$5000.00"
    image_urls = [
        "retail/images/product-images/product-image_1.webp",
        "retail/images/product-images/product-image_2.webp",
        "retail/images/product-images/product-image_3.webp",
        "retail/images/product-images/product-image_4.webp",
        "retail/images/product-images/product-image_5.webp",
    ]
    return render(
        request,
        "retail/product-details.html",
        {
            "product_name": product_name,
            "product_price": product_price,
            "image_urls": image_urls,
        },
    )


def wishlist(request):
    return render(request, "retail/wishlist.html")
