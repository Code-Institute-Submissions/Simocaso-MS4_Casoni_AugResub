from django.contrib import admin
from .models import Info

# Register your models here.

# groups by column the membership table in the admin tab


# class ProductAdmin(admin.ModelAdmin):

#     list_display = (
#         'pk',
#         'name',
#         'description',
#         'price',
#         'has_sizes',
#         'image_url',
#         'image',
#         )


admin.site.register(Info)
