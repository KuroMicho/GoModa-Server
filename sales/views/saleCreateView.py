from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from products.models import Product
from sales.models.sale import Sale
from sales.serializers import SaleSerializer
from users.permissions import IsVendorUser


class SaleCreateView(generics.CreateAPIView):

    serializer_class = SaleSerializer
    permission_classes = (IsAuthenticated, IsVendorUser)

    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({"status": "Not JSON"}, status=status.HTTP_400_BAD_REQUEST)

        query = Product.objects.filter(id=kwargs.get("product_id"))

        serializer = SaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            no_pass_threshold = int(query.first().inventory_onhand) > 0 and int(
                query.first().inventory_onhand
            ) >= int(request.data.get("number_shipments"))
        except Exception as e:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if no_pass_threshold:

            serializer.save()
            sale = Sale.objects.latest("id")
            
            if sale.number_shipments <= 0:
                return Response({"status": "Number not acceptable"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            query.update(inventory_shipped=F("inventory_shipped") + sale.number_shipments)
            query.update(inventory_onhand=F("inventory_onhand") - sale.number_shipments)

            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        return Response({"status": "No products available"}, status=status.HTTP_400_BAD_REQUEST)
