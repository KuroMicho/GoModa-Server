from rest_framework.response import Response
from rest_framework import generics, status
from products.models.product import Product
from products.serializers.productSerializer import ProductSerializer


class ProductsRetrieveView(generics.RetrieveAPIView):

    queryset =  Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)