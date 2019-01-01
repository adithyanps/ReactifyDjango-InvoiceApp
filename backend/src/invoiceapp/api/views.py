from rest_framework.generics import (
						ListAPIView,
						RetrieveUpdateDestroyAPIView,
						ListCreateAPIView,
						RetrieveAPIView)
from invoiceapp.models import (
							Customer,Items,
							P_Invoice,Child_Invoice
							)
from .serializers import (
					CustomerSerializer,ItemsSerializer,
					P_InvoiceSerializer,C_InvoiceSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Q

class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ItemsListView(ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class P_InvoiceListView(ListCreateAPIView):
	queryset = P_Invoice.objects.all()
	serializer_class = P_InvoiceSerializer

class P_InvoiceDetailView(RetrieveUpdateDestroyAPIView):
	queryset = P_Invoice.objects.all()
	serializer_class = P_InvoiceSerializer

class C_InvoiceListView(ListCreateAPIView):
	queryset = Child_Invoice.objects.all()
	serializer_class = C_InvoiceSerializer

class C_InvoiceDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Child_Invoice.objects.all()
	serializer_class = C_InvoiceSerializer
