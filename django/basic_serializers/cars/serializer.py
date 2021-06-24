from rest_framework import serializers
from cars.models import Cars

# model serializer
class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"