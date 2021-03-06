from django.db import models


class Membership(models.Model):

    class Meta:
        verbose_name_plural = 'Memberships'

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    text = models.CharField(max_length=3000, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
