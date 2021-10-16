from rest_framework.response import Response
from rest_framework import generics, status
from purchases.models.purchase import Purchase
from purchases.serializers.purchaseSerializer import PurchaseSerializer


class PurchasesRetrieveSupplierView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        queryset = Purchase.objects.filter(supplier=kwargs.get('supplier_id'))
        serializer = PurchaseSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)