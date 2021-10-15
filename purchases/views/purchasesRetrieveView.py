from rest_framework.response import Response
from rest_framework import generics, status
from purchases.models.purchase import Purchase
from purchases.serializers.purchaseSerializer import PurchaseSerializer


class PurchasesRetrieveView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        queryset = Purchase.objects.filter(product=kwargs.get('product_id')).all()
        serializer = PurchaseSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)