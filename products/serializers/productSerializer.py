from rest_framework import serializers
from products.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ["barcode", "name", "description", "color", "material", "size", "price", "minimum_required"]
        