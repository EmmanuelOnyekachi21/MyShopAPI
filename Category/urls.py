"""
URL configuration for the Category app.

This module defines the URL patterns for category-related views.
"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.category_list, name='category_list'),
]
