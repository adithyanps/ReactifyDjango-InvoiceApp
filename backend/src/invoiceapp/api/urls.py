from django.urls import path
from .views import (
            CustomerListView,CustomerDetailView,
            ItemsListView,ItemsDetailView,
            P_InvoiceListView,P_InvoiceDetailView,
            C_InvoiceListView,C_InvoiceDetailView
            )

urlpatterns = [
path('customer/',CustomerListView.as_view()),
path('customer/<pk>/',CustomerDetailView.as_view()),
path('items/',ItemsListView.as_view()),
path('items/<pk>/',ItemsDetailView.as_view()),
path('parent/',P_InvoiceListView.as_view()),
path('parent/<pk>/',P_InvoiceDetailView.as_view()),
path('child/',C_InvoiceListView.as_view()),
path('child/<pk>/',C_InvoiceDetailView.as_view())
]
