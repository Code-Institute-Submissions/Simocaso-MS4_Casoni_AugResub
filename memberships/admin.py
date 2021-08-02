from django.contrib import admin
from .models import Membership

# Register your models here.

# groups by column the membership table in the admin tab


class MembershipAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'text',
        'price',
        'image_url',
        'image',
        )


admin.site.register(Membership, MembershipAdmin)
