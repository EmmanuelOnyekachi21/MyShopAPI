"""
Products App Models

This module defines the database model 4 products in an eCommerce application.

The Product model includes fields for:
- Name, slug, and description
- Price, image, stock availability, and category
- Creation and modification timestamps

It also ensures unique product names and auto-generates slugs if not provided.
"""


from django.db import models
from django.utils.text import slugify
from Category.models import Category


class Product(models.Model):
    """
    Represents a product in the eCommerce store.

    Attributes:
        product_name (str): The name of the product (unique).
        slug (str): A URL-friendly identifier for the product.
        description (str): A brief description of the product (optional).
        price (int): The price of the product.
        image (ImageField): An optional image of the product.
        stock (int): The number of available items.
        is_available (bool): Indicates if d product is available for purchase
        category (ForeignKey): refers to the category the product belongs to.
        date_created (datetime): The timestamp when the product was created.
        date_modified (datetime): timestamp when d product was last modified.
    """
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='photos/products', blank=True, null=True
    )
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    available_colors = models.JSONField(default=list, blank=True)
    available_sizes = models.JSONField(default=list, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the product."""
        return self.product_name

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to\
            auto-generate a slug if not provided.

        If a product with the same slug already exists\
            a unique slug is created by appending a counter.
        """
        if not self.slug:
            slug = slugify(self.product_name)
            base_slug = slug

            count = 1

            while Product.objects.filter(slug=base_slug).exists():
                slug = f"{slug}-{count}"
                count += 1

            self.slug = slug
        super().save(*args, **kwargs)
