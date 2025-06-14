from django import forms 
from main.models import Order

class BasketAddproductForm(forms.Form):
    count = forms.IntegerField(min_valuet=1, max_value=255, initial=1, label='Колличество', widget=forms.NumberInput(attrs=['class':'form-control']))

