from rest_framework import serializers
from products.models.product import Product


class ProductInventorySerializer(serializers.ModelSerializer):
    
    color = serializers.JSONField()
    material = serializers.JSONField()
    class Meta:
        model = Product
        fields = '__all__'
        