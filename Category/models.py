#!/usr/python3

"""
Category App Models

This module defines the database model\
    for product categories in an eCommerce app.
It includes fields for category name, slug, description, and an optional image.
"""


from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Represents a product category.

    Attributes:
        category_name (str): The name of the category (max length: 50).
        slug (str): A unique slug for the category (max length: 100).
        description (str): A text description of the category.
        cat_image (ImageField): An optional image for the category,
                                uploaded to 'photos/categories/'
    """
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
            str: The category name.
        """
        return self.category_name

    class Meta:
        """
        Meta options for the Category model.
        """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        """
        Saves the category instance, ensuring a unique slug is generated
        if not provided.

        The slug is generated automatically using `slugify(category_name)`.
        If a duplicate slug exists, a numeric suffix\
            is added to ensure uniqueness.

        Example:
            - "electronics" → "electronics"
            - "electronics" (duplicate) → "electronics-1"

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.slug:
            slug_value = slugify(self.category_name)
            slug = slug_value

            counter = 1

            while Category.objects.filter(slug=slug).exists():
                slug = f"{slug_value}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)
