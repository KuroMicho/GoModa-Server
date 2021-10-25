from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from products.models.product import Product
from products.serializers.productInventorySerializer import ProductInventorySerializer


class ProductsRetrieveOnhandView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductInventorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)    
    
    search_fields  = ['color', 'material', 'size']
    filterset_fields = {
        'name': ['icontains'],
        'inventory_received': ['gt', 'lt', 'gte', 'lte'],
        'minimum_required': ['gt', 'lt', 'gte', 'lte'],
        'inventory_onhand': ['gt', 'lt', 'gte', 'lte'],
        'inventory_shipped': ['gt', 'lt', 'gte', 'lte']
    }

