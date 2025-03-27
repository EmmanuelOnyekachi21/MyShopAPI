"""
Admin configuration for the Category model.

This module customizes the Django admin interface for managing
categories, including how they are displayed and edited.
"""


from django.contrib import admin
from .models import Category
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the `Category` model.

    This class customizes how category objects are displayed
    and managed in the Django admin panel.

    Attributes:
        list_display (tuple): Fields displayed in the category list view.
        prepopulated_fields (dict): Fields that should be auto-filled
                                    based on other fields.
    """
    list_display = ("category_name", "slug", "cat_image")
    prepopulated_fields = {"slug": ("category_name",)}


admin.site.register(Category, CategoryAdmin)
