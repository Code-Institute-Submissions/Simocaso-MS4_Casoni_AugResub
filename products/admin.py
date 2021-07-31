from django.contrib import admin
from .models import Product

# Register your models here.

# groups by column the membership table in the admin tab


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'price',
        'has_sizes',
        'image_url',
        'image',
        )


admin.site.register(Product, ProductAdmin)
