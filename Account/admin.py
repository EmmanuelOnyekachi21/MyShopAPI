"""
admin.py

This module configures the Django admin panel for managing the `Account` model
It customizes how user accounts are displayed and managed within the admin
interface.
"""


from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    """
    Custom admin configuration for the Account model.

    This class customizes the display of user accounts in the Django
    admin panel. It defines how account-related fields are displayed,
    searched, filtered, and ordered.

    Attributes:
        list_display (tuple): Fields displayed in the admin user list.
        list_filter (tuple): Fields available for filtering.
        search_fields (tuple): Fields searchable in the admin panel.
        ordering (tuple): Default ordering for the user list.
        fieldsets (tuple): Sections and fields displayed when editing a user.
        add_fieldsets (tuple): Fields required when adding a new user.
        filter_horizontal (tuple): Fields that use horizontal filter widgets.
        readonly_fields (tuple): Fields that are read-only in the admin panel.
    """
    list_display = (
        'email', 'username', 'first_name', 'last_name', 'phone_number',
        'is_admin', 'is_staff', 'is_superadmin'
    )
    list_filter = ('is_active', 'is_admin', 'is_staff', 'email')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('-date_joined',)

    fieldsets = (
        ("Personal Information", {
            "fields": (
                "first_name", "last_name", "email", "username", "phone_number"
            )
        }),
        ("Permissions", {
            "fields": (
                "is_active", "is_staff", "is_admin", "is_superadmin"
            )
        }),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
 
    add_fieldsets = (
        ("Create New User", {
            "classes": ("wide",),
            "fields": (
                "email", "username", "first_name", "last_name",
                "phone_number", "password1", "password2"
            ),
        }),
    )

    filter_horizontal = ()
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(Account, AccountAdmin)
admin.site.site_header = "ShopRite Admin Panel"
admin.site.site_title = "ShopRite Admin"
admin.site.index_title = "Welcome to the ShopRite Admin Dashboard"
