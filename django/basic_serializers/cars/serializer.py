from django.core import serializers
from cars.models import Cars

# simplest example
# serializers object + serialize method + parameters: format + model
data = serializers.serialize("json", Cars.objects.all())
