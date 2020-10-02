from django.db import models



class product(models.Model):
    name_of_product = models.CharField(blank=False, max_length=200)

    quantity_of_product = models.IntegerField(blank=False)

    gst = models.IntegerField(blank=False, default=18)

    rate_of_product = models.IntegerField(blank=False)
