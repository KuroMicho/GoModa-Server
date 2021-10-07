from django.db import models

class Supplier(models.Model):
    supplier_id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length = 30)
    phone = models.CharField('Phone', max_length=16)
    email = models.EmailField('Email', max_length = 100)
    address = models.CharField('Address', max_length = 30)
    city = models.CharField('City', max_length = 20)
