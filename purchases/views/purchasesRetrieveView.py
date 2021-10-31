from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from purchases.models.purchase import Purchase
from products.models.product import Product
from purchases.serializers.purchaseSerializer import PurchaseSerializer
from users.permissions import IsVendorUser


class PurchasesRetrieveView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated, IsVendorUser)

    def get(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=kwargs.get("product_id"))
        except Exception as e:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        queryset = Purchase.objects.filter(product=product.id).all()
        serializer = PurchaseSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)