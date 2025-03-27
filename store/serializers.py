"""
Products App Serializers

This module defines serializers for the Product model\
    using Django REST Framework.

Serializers:
- `ProductSerializer`: Basic serializer for listing\
    and retrieving product details.
- `ProductDetailSerializer`: Extends `ProductSerializer`\
    with additional fields, such as similar products.
"""
from rest_framework import serializers
from .models import Product
from django.shortcuts import get_object_or_404
from Category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes the `Product` model for basic product representation.

    Attributes:
        category (CategorySerializer): Nested serializer for the product\
            category.
    """
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'description', 'price', 'slug', 'image',
            'stock', 'category'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Serializes the `Product` model with additional details.

    Attributes:
        similar_products (list): A list of products within the same category.
    """

    similar_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'description', 'price', 'image', 'stock',
            'similar_products', 'available_colors', 'available_sizes',
        ]

    def get_similar_products(self, product):
        """
        Retrieves products from the same category, excluding\
            the current product.

        Args:
            product (Product): The product instance.

        Returns:
            list: A serialized list of similar products.
        """
        products = Product.objects.filter(
            category__slug=product.category.slug,
            is_available=True
        ).exclude(id=product.id)
        serializer = ProductSerializer(products, many=True)
        return serializer.data
