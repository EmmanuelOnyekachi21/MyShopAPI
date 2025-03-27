"""
Serializers for the Category model.

This module defines the serializer for the `Category` model,
converting model instances to JSON format and vice versa.
"""

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the `Category` model.

    This serializer converts `Category` model instances into
    JSON format and handles deserialization for API requests.

    Meta:
        model (Category): The model being serialized.
        fields (list): The fields to be included in the serialized output.
    """
    class Meta:
        """
        Meta class.
        """
        model = Category
        fields = ['id', 'category_name', 'slug']
