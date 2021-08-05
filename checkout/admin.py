# from django.contrib import admin
# from .models import Order, OrderLineItem

# # Register your models here.


# class OrderLineItemAdminInline(admin.TabularInline):
#     model = OrderLineItem
#     readonly_fields = ('lineitem_total',)

#     # order_number
#     # full_name
#     # email
#     # phone_number
#     # country
#     # postcode
#     # town_or_city
#     # address
#     # date
#     # delivery
#     # order_total
#     # final_total


# class OrderAdmin(admin.ModelAdmin):
#     inlines = (OrderLineItemAdminInline,)

#     readonly_fields = ('order_number', 'date', 'delivery',
#                        'order_total', 'final_total',)

#     fields = ('order_number', 'date', 'full_name',
#               'email', 'phone_number', 'country',
#               'postcode', 'town_or_city', 'address',
#               'delivery', 'order_total', 'final_total')

#     list_display = ('order_number', 'date', 'full_name',
#                     'order_total', 'delivery', 'final_total',)

#     ordering = ('-date',)


# admin.site.register(Order, OrderAdmin)
