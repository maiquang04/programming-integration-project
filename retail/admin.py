from django.contrib import admin
from .models import (
    User,
    Category,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Address,
    Wishlist,
    WishlistItem,
)


# Register models
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_customer", "is_admin", "is_staff")
    list_filter = ("is_customer", "is_admin", "is_staff")
    search_fields = ("username", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "icon")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "category")
    search_fields = ("name", "description")
    list_filter = ("category",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__username",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    search_fields = ("product__name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "total_amount",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("user__username",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")
    search_fields = ("product__name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "company_name", "street_address", "apartment_floor", "city", "phone_number", "email_address")
    search_fields = ("first_name", "street_address", "city", "phone_number", "email_address")


admin.site.register(Wishlist)
admin.site.register(WishlistItem)
