from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from suppliers.models.supplier import Supplier
from suppliers.serializers import SupplierSerializer


'''
supplier_create     POST a new supplier
'''
@api_view(['POST'])
def supplier_create(request):
    if request.method == 'POST':
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
supplier_list   GET all supplier's list
'''
@api_view(['GET'])
def supplier_list(request):
    if request.method == 'GET':
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return Response(serializer.data)


'''
supplier_get    GET a supplier
'''
@api_view(['GET'])
def supplier_get(request, pk):
    
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)


'''
supplier_put    UPDATE a supplier
'''
@api_view(['PUT'])
def supplier_put(request, pk):
    
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
supplier_delete     DELETE a supplier
'''
@api_view(['DELETE'])
def supplier_delete(request, pk):
    
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)