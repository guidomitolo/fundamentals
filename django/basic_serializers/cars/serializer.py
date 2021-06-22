from django.core import serializers as django_serializers
from rest_framework import serializers
from cars.models import Cars

# simplest example
# serializers object + serialize method + parameters: format + model
data = django_serializers.serialize("json", Cars.objects.all())

# model serializer
class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        # fields = "__all__"
        fields = ['model', 'vendor', 'date', 'price', 'condition']