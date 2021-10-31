from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from products.models.product import Product
from products.serializers.productSerializer import ProductSerializer
from users.permissions import IsVendorUser


class ProductsRetrieveView(generics.RetrieveAPIView):
    
    permission_classes = (IsAuthenticated, IsVendorUser)

    queryset =  Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)