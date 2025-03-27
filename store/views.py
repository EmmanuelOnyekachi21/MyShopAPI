"""
Products App Views

This module defines API views for retrieving product information.

Views:
- `product_list`: Retrieves all available products or filters by category.
- `product_details`: Retrieves detailed information about a specific product.
"""
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def product_list(request, category_slug=None):
    """
    Retrieves a list of available products.

    If a `category_slug` is provided, filters products by category.

    Args:
        request (HttpRequest): The HTTP request object.
        category_slug (str, optional): The slug of the category to\
            filter products.

    Returns:
        Response: A JSON response containing the serialized product data.
    """
    if category_slug:
        products = Product.objects.filter(
            category__slug=category_slug, is_available=True
        )
    else:
        products = Product.objects.filter(is_available=True)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_details(request, category_slug, product_slug):
    """
    Retrieves detailed information about a specific product.

    Args:
        request (HttpRequest): The HTTP request object.
        category_slug (str): The slug of the category the product belongs to.
        product_slug (str): The slug of the product.

    Returns:
        Response: A JSON response containing the serialized product details.
    """
    product = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug
    )
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)
