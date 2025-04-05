"""
Cart App Models

This module defines the database models for the cart and cart items in the
ecommerce application. The Cart model represents a shopping cart, while
the CartItem model represents individual products within a cart.
"""

from django.db import models
from django.conf import settings
import uuid

from store.models import Product


class Cart(models.Model):
    """
    Represents a shopping cart.

    Each cart has a unique UUID code,
    and may be optionally associated with a user.
    Carts are marked as 'paid' once a purchase is completed.
    """
    cart_code = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cart_code)


class CartItem(models.Model):
    """
    Represents an item inside a Cart.

    Each CartItem is linked to a Cart and a Product. It keeps track of the
    quantity of the product added to the cart.
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.quantity} x {self.product.product_name}'
