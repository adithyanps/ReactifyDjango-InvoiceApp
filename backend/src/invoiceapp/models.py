from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.name
class Items(models.Model):
    item = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.item
class P_Invoice(models.Model):
    # id= models.IntegerField(null=False, )
    name = models.CharField(max_length=50,null=False)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    invoice_number = models.IntegerField(unique=True,null=False,primary_key=True)
    def __str__(self):
        return '%s %s'%(self.name,self.invoice_number)
class Child_Invoice(models.Model):
    invoice_number = models.ForeignKey(P_Invoice,db_constraint=True,on_delete=models.CASCADE)
    item = models.CharField(max_length=60,null=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    quantity = models.IntegerField(null=False)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.invoice_number
