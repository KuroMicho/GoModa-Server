from rest_framework.response import Response
from rest_framework import generics, status
from products.models.product import Product
from products.serializers.productSerializer import ProductSerializer


class ProductCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        
    