from suppliers.models.supplier import Supplier
from rest_framework import serializers

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        #fields = '__all__'
        #fields = ['id','name', 'address', 'phone', 'email', 'city']
        fields = ['name', 'address', 'phone', 'email', 'city']

#Los serializers son clases que nos permiten transformar datos de 
#formatos propios de Django, en formato del entorno web (JSON en este caso)
     