from .models import product
from django import forms

class product_details(forms.ModelForm):
    class Meta:
        model =product
        fields=[
            'name_of_product',
            'quantity_of_product',
            'gst',
            'rate_of_product',
]