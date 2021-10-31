from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from products.models.product import Product
from products.serializers.productSerializer import ProductSerializer


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if not request.data:
            return Response({"status": "Not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if not request.data:
            return Response({"status": "Not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        no_ignore = ["color", "material"]

        request_payload = {}
        for key, value in request.data.items():
            if key in no_ignore:
                request_payload[key] = value

        serializer = ProductSerializer(
            product, data=request_payload, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({}, status=status.HTTP_200_OK)
