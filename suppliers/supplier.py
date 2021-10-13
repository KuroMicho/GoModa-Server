from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=30, blank=False)
    address = models.TextField()
    phone = models.CharField(max_length=16, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    city = models.CharField(max_length=20)
