from django.contrib import admin
from .models import Customer,Items ,P_Invoice,Child_Invoice#
# Register your models here.
admin.site.register(Customer)
admin.site.register(Items)
admin.site.register(P_Invoice)
admin.site.register(Child_Invoice)
