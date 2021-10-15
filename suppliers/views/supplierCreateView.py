from rest_framework.response import Response
from rest_framework import generics, status
from suppliers.serializers.supplierSerializer import SupplierSerializer


class SupplierCreateView(generics.CreateAPIView):

    serializer_class = SupplierSerializer
    def post(self, request, *args, **kwargs):

        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)