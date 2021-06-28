from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User


class BooksSerializer(serializers.ModelSerializer):

    # only authorized librarians would be able to make api requests

    # The source argument controls which attribute is used to populate a field, 
    # and can point at any attribute on the serialized instance. 
    librarian = serializers.ReadOnlyField(source='librarian.username')

    # ReadOnlyField will not be used for updating model instances when they are deserialized. 
    # We could have also used CharField(read_only=True) here.

    class Meta:
        model = Books
        fields = '__all__'
        # fields = ['librarian', 'author', 'title', 'genre', 'price']

    def create(self, validated_data):
        print('serializer->Create')
        print(validated_data)
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    # reverse relationship to books
    # ¿Which books did the librarian loaded?
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Books.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'books']