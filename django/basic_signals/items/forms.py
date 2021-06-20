from django import forms

from .models import Order, Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'unit_price', 'quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['stock_item', 'quantity']

    # product = forms.ModelChoiceField(
    #     queryset=Stock.objects.all(), 
    #     # to_field_name='product',
    #     # required=True
    # )