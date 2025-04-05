"""
Cart App URL Configuration

This module defines the URL patterns for the cart app. Each path maps
to a view responsible for managing cart-related operations such as
adding items, retrieving the cart, checking cart contents, and removing items.
"""

from . import views
from django.urls import path

urlpatterns = [
    # Add an item to the cart
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

    # Check if a specific item is already in the cart
    path('item_in_cart/', views.item_in_cart, name='item_in_cart'),

    # Get the number of items currently in the cart
    path('get_num_of_items/', views.get_num_of_items, name='get_num_of_items'),

    # Retrieve the full cart including items and total price
    path('get_cart/', views.get_cart, name='get_cart'),

    # Remove an item from the cart
    path('remove_cart_item', views.remove_cart_item, name='remove_cart_item')
]
