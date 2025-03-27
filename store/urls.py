"""
Products App URLs

This module defines URL patterns for the Products app.

Routes:
- `/` → List all products or filter by category (optional).
- `/<category_slug>/` → List products within a specific category.
- `/<category_slug>/<product_slug>/` → Retrieve details of a specific product.
"""

from . import views
from django.urls import path


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),
    path(
        '<slug:category_slug>/<slug:product_slug>/',
        views.product_details,
        name='product_details'
    ),
]
