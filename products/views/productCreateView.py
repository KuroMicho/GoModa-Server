from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from products.serializers.productSerializer import ProductSerializer


class ProductCreateView(generics.CreateAPIView):

    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, serializer.data, status=status.HTTP_201_CREATED)

        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        
    