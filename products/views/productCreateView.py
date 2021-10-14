from rest_framework.response import Response
from rest_framework import generics, status
from products.serializers.productSerializer import ProductSerializer


class ProductCreateView(generics.CreateAPIView):

    serializer_class = ProductSerializer
    def post(self, request, *args, **kwargs):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        
    