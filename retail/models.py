from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg, Count


# Custom User model
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


# Category model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(
        upload_to="retail/categories/icons/", blank=True, null=True
    )

    def get_icon(self):
        if self.icon:
            return self.icon.url
        return "/static/retail/images/default-category.svg"

    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="retail/products/", blank=True, null=True
    )
    image_url = models.URLField(max_length=500, blank=True, null=True)
    sold_quantity = models.PositiveIntegerField(default=0)

    def get_image(self):
        if self.image_url:
            return self.image_url
        elif self.image:
            return self.image.url
        return "/static/retail/images/default-product.png"

    def get_price(self):
        return self.discounted_price if self.discounted_price else self.price

    def average_rating(self):
        return self.ratings.aggregate(Avg("rating"))["rating__avg"] or 0

    def total_ratings(self):
        return self.ratings.aggregate(Count("id"))["id__count"]

    def __str__(self):
        return self.name


# Cart model
class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name="cart", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


# CartItem model
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="cart_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.product.get_price()

# Order model
class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE
    )
    PAYMENT_CHOICES = [
        ("Card", "Card"),
        ("Cash on Delivery", "Cash on Delivery"),
    ]
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Pending"
    )
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_CHOICES, default="Cash on Delivery"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"


# OrderItem model
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price


# Address model
class Address(models.Model):
    user = models.ForeignKey(
        User, related_name="addresses", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True, null=True,default='')  # Optional
    street_address = models.CharField(max_length=255)
    apartment_floor = models.CharField(max_length=255, blank=True, null=True,default='')  # Optional
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(default='example@example.com')

    def __str__(self):
        return f"{self.first_name}, {self.street_address}, {self.city}, {self.phone_number}"


# Wishlist model
class Wishlist(models.Model):
    user = models.ForeignKey(
    User,  # Reference to the User model
    related_name="wishlist",  # Backward relation name for reverse queries
    on_delete=models.CASCADE,  # Delete the wishlist items when the user is deleted
    null=False,  # Ensures the field is NOT NULL in the database
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist of {self.user.username}"


# WishlistItem model
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, 
        related_name="items", 
        on_delete=models.CASCADE,
        null=False,
    )
    product = models.ForeignKey(
        Product, related_name="wishlist_items", on_delete=models.CASCADE, null= False,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.product.name} in {self.wishlist.user.username}'s wishlist"
        )


class Rating(models.Model):
    product = models.ForeignKey(
        Product, related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="ratings", on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.product.name} - {self.rating} star(s)"
