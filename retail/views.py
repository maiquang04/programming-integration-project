from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Category, Product, Cart, CartItem, Address, Wishlist, WishlistItem, Order,OrderItem


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
    if not request.user.is_authenticated:
        return redirect("login")

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(
        item.product.get_price() * item.quantity for item in cart_items
    )
    context = {"cart_items": cart_items, "total_price": total_price}

    return render(request, "retail/cart.html", context)


def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    subtotal = sum(
        item.product.get_price() * item.quantity for item in cart_items
    )
    total = subtotal

    billing_details = Address.objects.filter(user=request.user).first()
    if request.method == "POST":
        # Update existing billing details or create new ones
        if billing_details:
            # Update existing details
            billing_details.first_name = request.POST["first_name"]
            billing_details.company_name = request.POST.get("company_name", "")
            billing_details.street_address = request.POST["street_address"]
            billing_details.apartment_floor = request.POST.get("apartment", "")
            billing_details.city = request.POST["city"]
            billing_details.phone_number = request.POST["phone_number"]
            billing_details.email_address = request.POST["email"]
        else:
            # Create new billing details
            billing_details = Address(
                user=request.user,
                first_name=request.POST["first_name"],
                company_name=request.POST.get("company_name", ""),
                street_address=request.POST["street_address"],
                apartment_floor=request.POST.get("apartment", ""),
                city=request.POST["city"],
                phone_number=request.POST["phone_number"],
                email_address=request.POST["email"],
            )
        billing_details.save()

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "Total": total,
        "billing_details": billing_details,
    }

    return render(request, "retail/checkout.html", context)


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    related_products = Product.objects.filter(category=product.category)[:4]
    # Check if the product is already in the user's wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    is_in_wishlist = wishlist.items.filter(product=product).exists()
    return render(
        request,
        "retail/product-details.html",
        {
            "product": product,
            "is_in_wishlist":is_in_wishlist,
            "related_products": related_products,
        },
    )


def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = Product.objects.filter(wishlist_items__wishlist=wishlist)
    return render(request, "retail/wishlist.html",
                {
                    'wishlist_items': wishlist_items
                })


def category(request, category_id):
    categories = Category.objects.all()

    category = Category.objects.get(pk=category_id)
    products = category.products.all()

    context = {
        "categories": categories,
        "category": category,
        "products": products,
    }

    return render(request, "retail/category.html", context)


def all_products(request):
    categories = Category.objects.all()

    products = Product.objects.all()

    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "retail/category.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        return redirect("login")
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )
    quantity = int(request.POST.get("quantity", 1))
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect("cart")

def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        return redirect("login")
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlistItem , createdItem = WishlistItem.objects.get_or_create(wishlist=wishlist,product=product)
    if createdItem :
        wishlistItem.save()
    else:
        wishlistItem.delete()
    return redirect("product-details",product_id=product_id)

def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlistItem , createdItem = WishlistItem.objects.get_or_create(wishlist=wishlist,product=product)
    wishlistItem.delete()
    return redirect("wishlist")

def move_all_to_bag(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    wishlist_products = WishlistItem.objects.filter(wishlist=wishlist)
    for wishlist_product in wishlist_products:
        cart_item, createdCartItem = CartItem.objects.get_or_create(
            cart=cart, product= wishlist_product.product
        )
        if not createdCartItem:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()
        wishlist_product.delete()
    return redirect('cart')

def remove_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect("cart")


def update_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.cart.user == request.user:
        new_quantity = int(request.POST.get("quantity"))
        if new_quantity >= 1 and new_quantity <= cart_item.product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()
    return redirect("cart")


def search(request):
    query = request.GET.get("q")
    products = Product.objects.filter(name__icontains=query)
    return render(
        request, "retail/search.html", {"products": products, "query": query}
    )

def place_order(request):

    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect("cart")

    # Collect cart items and calculate total
    cart_items = CartItem.objects.filter(cart=cart)
    total_amount = sum(item.product.get_price() * item.quantity for item in cart_items)

    # Get payment method from POST request
    payment_method = request.POST.get("payment_method", "Cash on Delivery")

    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        payment_method=payment_method,
        status="Pending"
    )

    # Create order items
    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.product.get_price()
        )
        # Reduce stock for the product
        cart_item.product.stock -= cart_item.quantity
        cart_item.product.save()

    # Clear the cart after placing the order
    cart_items.delete()

    return redirect("index")