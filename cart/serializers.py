"""
Cart and CartItem App Serializers

This module defines serializers for the Cart and CartItem models, which
are used to convert model instances into JSON representations and vice versa.

Serializers:
- CartItemSerializer: Serializes individual items in the cart.
- CartSerializer: Serializes the entire cart with all items.
- SimpleCartSerializer: Serializes minimal cart details\
    such as cart code and total item count.
"""

from rest_framework import serializers
from .models import Cart, CartItem
from store.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.

    Serializes cart item fields,\
        including product details and the calculated item price.
    """
    product = ProductSerializer(read_only=True)
    item_price = serializers.SerializerMethodField()

    class Meta:
        """
        Meta configuration for CartItemSerializer.
        Specifies the model and fields to include in the serialized output.
        """
        model = CartItem
        fields = [
            'id', 'quantity', 'cart', 'product', 'item_price'
        ]

    def get_item_price(self, cartitem):
        """
        Calculate the total price for a cart item based on\
            quantity and product price.
        """
        return cartitem.quantity * cartitem.product.price


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.

    Serializes a complete cart instance including its items and total price.
    """
    items = CartItemSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        """
        Meta configuration for CartSerializer.
        Specifies the model and fields to include in the serialized output.
        """
        model = Cart
        fields = [
            'id', 'cart_code', 'total_price', 'items'
        ]

    def get_total_price(self, cart):
        """
        Compute the total price of all items in the cart.
        """
        return sum([
            item.quantity * item.product.price
            for item in cart.items.all()
        ])


class SimpleCartSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for the Cart model.

    Provides a lightweight version with only the cart ID, cart code,
    and the number of items in the cart.
    """
    num_of_items = serializers.SerializerMethodField()

    class Meta:
        """
        Meta configuration for SimpleCartSerializer.
        Defines the model and selected fields to be serialized.
        """
        model = Cart
        fields = [
            'id', 'cart_code', 'num_of_items'
        ]

    def get_num_of_items(self, cart):
        """
        Calculate the total number of items (quantities summed) in the cart.
        """
        return sum([item.quantity for item in cart.items.all()])
