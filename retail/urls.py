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
    path(
        "product-details/<int:product_id>",
        views.product_details,
        name="product-details",
    ),
    path("wishlist", views.wishlist, name="wishlist"),
    path("category/<int:category_id>", views.category, name="category"),
    path("all-products", views.all_products, name="all-products"),
    path(
        "add-to-cart/<int:product_id>/", views.add_to_cart, name="add-to-cart"
    ),
    path(
        "add-to-wishlist/<int:product_id>/", views.toggle_wishlist, name="toggle-wishlist"
    ),
    path(
        "remove-from-wishlist/<int:product_id>/", views.remove_from_wishlist, name="remove-from-wishlist"
    ),
    path(
        "move-all-to-bag/", views.move_all_to_bag, name="move-all-to-bag"
    ),
    path(
        "update-cart-item/<int:item_id>/",
        views.update_cart_item,
        name="update-cart-item",
    ),
    path(
        "remove-cart-item/<int:item_id>/",
        views.remove_cart_item,
        name="remove-cart-item",
    ),
    path("search", views.search, name="search"),
]
