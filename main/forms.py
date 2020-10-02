from .models import data
from django import forms


class data_of_user(forms.ModelForm):
    class Meta:
        model = data
        fields = [
            'bill_number',
            'name',
            'date',
            'addres',
            'state',
        ]
class product_details(forms.ModelForm):
    class Meta:
        model =data
        fields=[
            'name_of_product',
            'quantity_of_product',
            'gst',
            'rate_of_product']