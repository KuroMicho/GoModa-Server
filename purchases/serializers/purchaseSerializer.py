from rest_framework import serializers
from purchases.models import Purchase
from products.models.product import Product
from suppliers.models.supplier import Supplier


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields= '__all__'
    
    def to_representation(self, obj):
        purchase    = Purchase.objects.get(id=obj.id)
        product = Product.objects.get(purchase=obj.id)
        supplier = Supplier.objects.get(purchase=obj.id)
        
        return {
            'purchase_id'    : purchase.id,
            'date_purchased' : purchase.date_purchased,
            'supplier' : {
                'name'  : supplier.name,
                'email' : supplier.email,
                'city'  : supplier.city                
            },
            'product' : {
                'id'               : product.id,
                'name'             : product.name,
                'price'            : product.price,
                'number_purchases' : purchase.number_purchases
            }
        }