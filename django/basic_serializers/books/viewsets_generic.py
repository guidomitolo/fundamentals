from django.shortcuts import render
from books.serializer import BooksSerializer, UserSerializer
from books.models import Books
from django.contrib.auth.models import User

from rest_framework import generics

# allow authenticated requests get read-write access
# and unauthenticated requests get read-only access.
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


# entrypoints to the APIs
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'librarians': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format)
    })


def books(request):
    books = Books.objects.all()
    return render(request, 'books/books.html', {'data':books})


# ViewSet classes are almost the same thing as View classes, 
# except that they provide operations such as 
# retrieve, or update, and not method handlers such as get or put.

# A ViewSet class is only bound to a set of method handlers at the last moment,
# when it is instantiated into a set of views, typically 
# by using a Router class which handles the complexities of defining the URL conf for you.

class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # overriding a .perform_create() method on our view
    # allows us to modify how the instance save is managed, and handle any information 
    # that is implicit in the incoming request or requested URL.

    def perform_create(self, serializer):
        serializer.save(librarian=self.request.user)


# detail + update + delete in one class view
class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # The user isn't sent as part of the serialized representation, 
    # but is instead a PROPERTY of the INCOMING request.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


