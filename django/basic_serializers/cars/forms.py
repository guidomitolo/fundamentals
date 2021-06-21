from django import forms
from cars.models import Cars
from basic_test import settings

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['model', 'vendor', 'date', 'price', 'condition']

        date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
