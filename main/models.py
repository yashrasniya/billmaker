from django.db import models
import datetime


# Create your models here.
class data(models.Model):
    bill_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(default=str(datetime.datetime.now())[:10])
    addres = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    name_of_product = models.CharField(blank=True,max_length=200)
    quantity_of_product = models.IntegerField(blank=True,default=20)
    gst = models.IntegerField(blank=True, default=18)
    rate_of_product = models.IntegerField(blank=True,default=20 )

