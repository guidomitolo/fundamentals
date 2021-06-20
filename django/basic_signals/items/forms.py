from django import forms

from .models import Order, Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'unit_price', 'quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'quantity']

    product = forms.ModelChoiceField(
        queryset=Stock.objects.values_list('product', flat=True).all(), 
        to_field_name='product',
        required=True
    )