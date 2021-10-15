from rest_framework.response import Response
from rest_framework import generics, status
from suppliers.models.supplier import Supplier
from suppliers.serializers.supplierSerializer import SupplierSerializer


class SuppliersRetrieveView(generics.RetrieveAPIView):

    queryset =  Supplier.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SupplierSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)