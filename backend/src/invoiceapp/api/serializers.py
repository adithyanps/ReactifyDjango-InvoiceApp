from rest_framework import serializers
from invoiceapp.models import Customer,Items ,P_Invoice,Child_Invoice

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name']
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id','item','price']
class P_InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_Invoice
        fields = '__all__'
        # fields = ['id','invoice_number','name','date','total_amount']
class C_InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Invoice
        fields = ['id','invoice_number','item','quantity','price','sub_total']
        # fields = '__all__'
