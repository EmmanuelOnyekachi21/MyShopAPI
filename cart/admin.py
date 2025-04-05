from django.contrib import admin
from cart.models import Cart, CartItem


# Create an Inline model for CartItem
class CartItemInline(admin.TabularInline):
    """
    Defines the inline admin interface for CartItem within the Cart admin view.
    Displays cart items in a tabular format when viewing a cart.
    """
    model = CartItem
    extra = 1  # Number of blank items shown for adding new entries


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Cart model.
    Includes inline display of associated cart items.
    """
    list_display = ['cart_code', 'created']
    search_fields = ['cart_code']
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for CartItem model.
    Enables searching and viewing cart items independently.
    """
    list_display = ['product', 'cart', 'quantity']
    search_fields = ['product__name', 'cart__cart_code']
