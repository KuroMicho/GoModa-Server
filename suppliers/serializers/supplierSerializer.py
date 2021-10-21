from suppliers.models.supplier import Supplier
from rest_framework import serializers

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'phone', 'email', 'city']
     