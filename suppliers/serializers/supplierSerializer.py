from rest_framework import serializers
from suppliers.models.supplier import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = ["name", "address", "phone", "email", "city"]