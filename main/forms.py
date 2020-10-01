from .models import data
from django import forms


class data_of_user(forms.ModelForm):
    class Meta:
        model = data
        fields = [
            'bill_number',
            'name',
            # 'date',
            'addres',
            'state',
        ]
