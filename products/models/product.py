from django.db import models


def jsonfield_default_value():
    return {}


class Product(models.Model):

    barcode = models.CharField(
        blank=False, unique=True, default="123456789", max_length=10
    )
    name = models.CharField(max_length=100, blank=False)
    image = models.URLField(blank=False, max_length=200)
    description = models.TextField(blank=True)
    color = models.JSONField(blank=True, default=jsonfield_default_value)
    material = models.JSONField(blank=True, default=jsonfield_default_value)
    size = models.JSONField(blank=True, default=jsonfield_default_value)
    price = models.FloatField(blank=False, default=0)
    inventory_received = models.IntegerField(blank=True, default=0)
    minimum_required = models.IntegerField(blank=False)
    inventory_onhand = models.IntegerField(blank=True, default=0)
    inventory_shipped = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
