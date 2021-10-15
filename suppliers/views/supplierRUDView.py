from rest_framework.response import Response
from rest_framework import generics, status
from suppliers.models.supplier import Supplier
from suppliers.serializers.supplierSerializer import SupplierSerializer


class SupplierRUDView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):

        try:
            supplier = Supplier.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(supplier)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        try:
            supplier = Supplier.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if not request.data:
            return Response({"status": "Not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SupplierSerializer(supplier, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):

        try:
            supplier = Supplier.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        supplier.delete()
        return Response({}, status=status.HTTP_200_OK)