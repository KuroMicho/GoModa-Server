from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from suppliers.models.supplier import Supplier
from suppliers.serializers import SupplierSerializer


@api_view(["POST"])
def supplier_create(request):
    """
    supplier_create     POST a new supplier
    """
    if request.method == "POST":
        serializer = SupplierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def supplier_list(request):
    """
    supplier_list   GET all supplier's list
    """
    if request.method == "GET":
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def supplier_get_put_delete(request, pk):
    """
    Retrieve, update and get a supplier by id
    """
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
