from django.db import models


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=60, null=False, editable=False)
    phone_number = models.CharField(max_length=60, null=False, editable=False)
    email_address = models.CharField(max_length=30, null=False, editable=False)
    address_1 = models.CharField(max_length=30, null=False, editable=False)
    address_2 = models.CharField(max_length=30, null=False, editable=False)
    postcode = models.CharField(max_length=30, null=False, editable=False)
    town_or_city = models.CharField(max_length=30, null=False, editable=False)
    county = models.CharField(max_length=30, null=False, editable=False)
    country = models.CharField(max_length=30, null=False, editable=False)
    date = models.CharField(max_length=30, null=False, editable=False)
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

    def __str__(self):
        return self.name
