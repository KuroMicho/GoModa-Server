from django.db.models import F
from rest_framework.response import Response
from rest_framework import generics, status
from sales.models.sale import Sale
from sales.serializers import SaleSerializer


class SalesRetrieveView(generics.RetrieveAPIView):

    def get(self, request, product_id, *args, **kwargs):

        queryset = Sale.objects.filter(product=product_id).all()
        serializer = SaleSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)