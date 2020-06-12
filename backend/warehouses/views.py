from django.shortcuts import render
from rest_framework import filters, exceptions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import WarehouseSerializer
from .models import Warehouse

class WarehouseViewset(viewsets.ModelViewSet):
    """Handle CRUD Views
    Methods: list, create, retrieve, 
    update, partial_update, destroy"""
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'barcode__id', 'datacom__id', 'partner__id', 'company__id']
    search_fields = ['id', 'barcode__id', 'datacom__id', 'partner__id', 'company__id']
    ordering_fields = '__all__'
    ordering = ['date_added']