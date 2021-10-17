from rest_framework.response import Response
from rest_framework import generics, status
from purchases.models.purchase import Purchase
from suppliers.models.supplier import Supplier
from purchases.serializers.purchaseSerializer import PurchaseSerializer


class PurchasesRetrieveSupplierView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        
        try:
            supplier = Supplier.objects.get(id=kwargs.get("supplier_id"))
        except Exception as e:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        queryset = Purchase.objects.filter(supplier=supplier.id)
        serializer = PurchaseSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
