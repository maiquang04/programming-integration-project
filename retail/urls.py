from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("product-details", views.product_details, name="product-details"),
    path("wishlist", views.wishlist, name="wishlist"),
]
