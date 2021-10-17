from rest_framework import serializers
from sales.models.sale import Sale
from products.models.product import Product


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def to_representation(self, obj):
        sale    = Sale.objects.get(id=obj.id)
        product = Product.objects.get(sale=obj.id)

        return {
            'sale_id'      : sale.id,
            'date_shipped' : sale.date_shipped,
            'product' : {
                'id'               : product.id,
                'name'             : product.name,
                'price'            : product.price,
                'number_shipments' : sale.number_shipments
            }
        }