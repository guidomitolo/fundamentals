from django.shortcuts import render
from books.serializer import BooksSerializer, UserSerializer
from books.models import Books
from django.contrib.auth.models import User

from rest_framework import generics

# allow authenticated requests get read-write access
# and unauthenticated requests get read-only access.
from rest_framework import permissions


def books(request):
    books = Books.objects.all()
    return render(request, 'books/books.html', {'data':books})


class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# detail + update + delete in one class view
class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # The user isn't sent as part of the serialized representation, 
    # but is instead a PROPERTY of the INCOMING request.

    # The way we deal with that is by overriding a .perform_create() method on our snippet views, 
    # that allows us to modify how the instance save is managed, and handle any information 
    # that is implicit in the incoming request or requested URL.

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


