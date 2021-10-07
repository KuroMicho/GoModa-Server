from supplierApp.models.supplier import Supplier
from rest_framework import serializers
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email', 'address','city']