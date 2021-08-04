import uuid

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from products.models import Product

# Code partly used from CI checkout lesson


class Order(models.Model):
    order_number = models.CharField(max_length=40, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email_address = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(blank_label='Country', null=False, blank=False)
    order_date = models.DateField("Order Date", auto_now_add=True)
    delivery = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)
    final_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)

    def _generate_order_number(self):
        """
        Function that generates a unique order number.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates cart total each time an order item is added
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.final_total = self.total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderlineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=2, null=True, blank=True)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'pk {self.product.pk} on order {self.order.order_number}'
