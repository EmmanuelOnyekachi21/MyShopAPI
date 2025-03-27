"""
Admin configuration for the Product model.

This module customizes the Django admin interface for managing products,
including handling JSON fields as comma-separated values.

"""
from django.contrib import admin
from .models import Product
from django import forms


class ProductAdminForm(forms.ModelForm):
    """
    Custom form for the Product model in the Django admin.

    This form processes JSON fields (`available_colors`, `available_sizes`)
    as comma-separated values for easier input.
    """

    available_colors = forms.CharField(
        required=False,
        help_text="Enter colors as comma-separated values\
            (e.g., Red, Blue, Green)"
    )

    available_sizes = forms.CharField(
        required=False,
        help_text="Enter sizes as comma-separated values (e.g., S, M, L, XL)"
    )

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and prepopulates JSON fields with\
            comma-separated values.
        """
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields["available_colors"].initial = (
                ", ".join(self.instance.available_colors)
                if self.instance.available_colors else ""
            )
            self.fields["available_sizes"].initial = (
                ", ".join(self.instance.available_sizes)
                if self.instance.available_sizes else ""
            )

    def clean_available_colors(self):
        """
        Cleans and converts the available_colors field
        from a comma-separated string to a JSON-compatible list.

        Returns:
            list: A list of cleaned color values.
        """
        colors = self.cleaned_data.get("available_colors", "")
        return [color.strip() for color in colors.split(",") if color.strip()]

    def clean_available_sizes(self):
        """
        Cleans and converts the available_sizes field
        from a comma-separated string to a JSON-compatible list.

        Returns:
            list: A list of cleaned size values.
        """
        sizes = self.cleaned_data.get("available_sizes", "")
        return [size.strip() for size in sizes.split(",") if size.strip()]


class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Product model.

    This class customizes how product objects are displayed
    and managed in the Django admin panel.

    Attributes:
        form (ProductAdminForm): Custom form for handling JSON fields.
        list_display (tuple): Fields displayed in the product list view.
        search_fields (tuple): Fields that can be searched in the admin panel.
        list_filter (tuple): Fields that can be filtered in the admin panel.
        prepopulated_fields (dict): Fields that should be auto-filled\
            based on other fields.
    """
    form = ProductAdminForm  # Ensure admin uses the custom form

    list_display = (
        "product_name", "price", "stock", "is_available", "category"
    )
    search_fields = ("product_name", "category__name")
    list_filter = ("is_available", "category")
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(Product, ProductAdmin)
