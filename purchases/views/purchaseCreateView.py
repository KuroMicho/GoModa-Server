from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from products.models.product import Product
from purchases.serializers.purchaseSerializer import PurchaseSerializer


class PurchaseCreateView(generics.CreateAPIView):
    
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({"status": "Not JSON"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(id=kwargs.get("product_id"))
        except Exception as e:
            print(e)
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            if int(request.data["number_purchases"]) <= 0:
                return Response({"status": "Number not acceptable"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            product.inventory_received += int(request.data["number_purchases"])
            product.save()
            
            if product.inventory_onhand == 0 and product.inventory_received > product.minimum_required:
                product.inventory_onhand = product.inventory_received - product.minimum_required
                product.save()
                
            elif product.inventory_onhand > 0:
                product.inventory_onhand += int(request.data["number_purchases"])
                product.save()
            
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)