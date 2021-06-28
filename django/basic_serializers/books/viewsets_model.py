from django.shortcuts import render
from books.serializer import BooksSerializer, UserSerializer
from books.models import Books
from django.contrib.auth.models import User

from rest_framework import viewsets

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

# With ModelViewSet class we can get the complete set of default read and write operations

class BooksList(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # overriding a .perform_create() method on our view
    # allows us to modify how the instance save is managed, and handle any information 
    # that is implicit in the incoming request or requested URL.

    def perform_create(self, serializer):
        serializer.save(librarian=self.request.user)


class UserList(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



