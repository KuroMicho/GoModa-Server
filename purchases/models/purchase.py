from django.db import models

from products.models import Product
from suppliers.models import Supplier


class Purchase(models.Model):

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    number_purchases = models.IntegerField()
