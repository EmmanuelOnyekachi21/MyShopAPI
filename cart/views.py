"""
Cart App Views

This module contains API views that manage the shopping cart functionality,
including adding items to the cart, checking if an item exists, retrieving
cart details, counting items, and removing items from the cart.

All views are decorated with @api_view for use with Django REST Framework.
"""

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart, CartItem
from cart.serializers import (
    CartItemSerializer, SimpleCartSerializer, CartSerializer
)
from store.models import Product


@api_view(['POST'])
def add_to_cart(request):
    """
    Adds a product to the cart. If the cart does not exist, it is created.

    Request data:
    - product_id: ID of the product to add
    - cart_code: Unique cart identifier (UUID)

    Returns:
    - CartItem data and success message, or error message
    """
    try:
        product_id = request.data.get('product_id')
        cart_code = request.data.get('cart_code')

        cart, _ = Cart.objects.get_or_create(cart_code=cart_code)
        product = get_object_or_404(Product, id=product_id)

        cartitem = CartItem(product=product, cart=cart, quantity=1)
        cartitem.save()

        serializer = CartItemSerializer(cartitem)
        return Response({
            'data': serializer.data,
            'message': 'Cart item created successfully',
        }, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
def item_in_cart(request):
    """
    Checks whether a specific product is already in the cart.

    Query parameters:
    - productId: ID of the product to check
    - cart_code: Unique cart identifier (UUID)

    Returns:
    - Boolean value (True if item exists, False otherwise)
    """
    try:
        product_id = request.query_params.get('productId')
        cart_code = request.query_params.get('cart_code')

        product = get_object_or_404(Product, id=product_id)
        cart = get_object_or_404(Cart, cart_code=cart_code)

        exists = CartItem.objects.filter(product=product, cart=cart).exists()
        return Response(exists)
    except Exception as e:
        return Response({'message': 'No item added to cart yet'})


@api_view(['GET'])
def get_num_of_items(request):
    """
    Retrieves the total number of items in the cart.

    Query parameters:
    - cart_code: Unique cart identifier (UUID)

    Returns:
    - Serialized cart object with item count
    """
    try:
        cart_code = request.query_params.get('cart_code')
        cart = get_object_or_404(Cart, cart_code=cart_code)

        serializer = SimpleCartSerializer(cart)
        return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})


@api_view(['GET'])
def get_cart(request):
    """
    Retrieves all items and the total price of a specific cart.

    Query parameters:
    - cart_code: Unique cart identifier (UUID)

    Returns:
    - Serialized cart with nested cart items and total price
    """
    try:
        cart_code = request.query_params.get('cart_code')
        cart = Cart.objects.get(cart_code=cart_code)

        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})


@api_view(['GET'])
def remove_cart_item(request):
    """
    Removes a specific item from the cart.

    Query parameters:
    - cart_code: Unique cart identifier (UUID)
    - product_id: ID of the product to remove

    Returns:
    - Updated cart data or error message
    """
    try:
        cart_code = request.query_params.get('cart_code')
        product_id = request.query_params.get('product_id')

        cart = Cart.objects.get(cart_code=cart_code)
        product = Product.objects.get(id=product_id)

        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        cart_item.delete()

        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})
