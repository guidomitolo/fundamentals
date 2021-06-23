from django.db.models import fields
from rest_framework import serializers
from .models import Houses

# serialization without ModelSerializer
class HousesSerializer(serializers.Serializer):
    # add id
    id = serializers.IntegerField(read_only=True)
    # model attr
    published = serializers.DateTimeField(required=False)
    street = serializers.CharField(max_length=64, allow_blank=True)
    adress = serializers.IntegerField()
    room = serializers.IntegerField()
    m2 = serializers.IntegerField()
    pool = serializers.BooleanField()
    price = serializers.FloatField()

    # https://www.django-rest-framework.org/api-guide/serializers/#saving-instances 
    def create(self, validated_data):
        return Houses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.published = validated_data.get('published', instance.published)
        instance.street = validated_data.get('street', instance.street)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.room = validated_data.get('room', instance.room)
        instance.pool = validated_data.get('pool', instance.pool)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

# Django Shell

# GET VS POST
# HousesSerializer(model_instance) != HousesSerializer(data=model_instance)