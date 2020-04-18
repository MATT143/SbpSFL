from django.db import models

# Create your models here.

class sflOrderLine(models.Model):
    salesOrderNo=models.CharField(max_length=20)
    offerName=models.CharField(max_length=20)
    quantity=models.IntegerField(default=100)
    subRefId=models.CharField(max_length=20)
    subscriptionId=models.CharField(max_length=20)
    prov_email=models.EmailField()
    deliveryMethod=models.CharField(max_length=10)
    sflProvStatus=models.CharField(max_length=20)

    def __str__(self):
        return self.salesOrderNo

