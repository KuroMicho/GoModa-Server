from django.contrib import admin

# Register your models here.

from .models.supplier import Supplier
admin.site.register(Supplier)