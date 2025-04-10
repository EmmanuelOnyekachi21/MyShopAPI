"""
Products App Views

This module defines API views for retrieving product information in the eCommerce system.

The available views are:
- `product_list`: Retrieves a paginated list of available products. Optionally filters products by category.
- `product_details`: Retrieves detailed information about a specific product.

These views interact with the `Product` model and its associated serializers to return product data as JSON responses.
"""
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET'])
def product_list(request, category_slug=None):
    """
    Retrieves a paginated list of available products.

    If a `category_slug` is provided, filters products by the category.

    Args:
        request (HttpRequest): The HTTP request object containing query parameters.
        category_slug (str, optional): The slug of the category to filter products by.

    Returns:
        Response: A paginated JSON response containing the list of serialized products.
    
    Pagination:
        This view supports pagination using the `PageNumberPagination` class.
        The number of products per page is set to 6.
    """
    if category_slug:
        products = Product.objects.filter(
            category__slug=category_slug, is_available=True
        )
    else:
        products = Product.objects.filter(is_available=True)
    paginator = PageNumberPagination()
    paginator.page_size = 6
    paginated_products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def product_details(request, category_slug, product_slug):
    """
    Retrieves detailed information about a specific product.

    Args:
        request (HttpRequest): The HTTP request object containing query parameters.
        category_slug (str): The slug of the category the product belongs to.
        product_slug (str): The slug of the product.

    Returns:
        Response: A JSON response containing the serialized details of the product.
    
    If the product does not exist in the specified category, a 404 error is raised.
    """
    product = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug
    )
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def query_product_list(request):
    query = request.query_params.get('query')
    
    if query:
        products = Product.objects.filter(product_name__icontains=query, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    paginator = PageNumberPagination()
    paginator.page_size = 6
    paginated_products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)
