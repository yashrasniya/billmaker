from django.db import models


# Create your models here.
class data(models.Model):
    bill_number = models.IntegerField()
    name = models.CharField(max_length=50)
    # date = models.DateField()
    addres = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
