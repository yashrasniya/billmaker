from django.db import models


# Create your models here.
class data(models.Model):
    bill_number = models.IntegerField( blank=True,null=True )
    name = models.CharField(max_length=50,null=True)
    # date = models.DateField(null=False)
    addres = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
