from django.db.models import F
from rest_framework.response import Response
from rest_framework import generics, status
from sales.models.sale import Sale
from products.models.product import Product
from sales.serializers import SaleSerializer


class SalesRetrieveView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("product_id"))
        except Exception as e:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        queryset = Sale.objects.filter(product=product.id).all()
        serializer = SaleSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)