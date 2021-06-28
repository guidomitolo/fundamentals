from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from books.viewsets_model import UserList, BooksList, api_root, books

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BooksList)
router.register(r'users', UserList)


# we're creating multiple views from each ViewSet class, 
# by binding the http methods to the required action for each view.

# book_list = BooksList.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# book_detail = BooksList.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# user_list = UserList.as_view({
#     'get': 'list'
# })
# user_detail = UserList.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns(
#     [
#         path('', books, name='books'),
#         path('api', api_root, name='api_books'),
#         path('books/', book_list, name='book-list'),
#         path('books/<int:pk>/', book_detail, name='book-detail'),
#         path('users/', user_list, name='user-list'),
#         path('users/<int:pk>/', user_detail, name='user-detail')
#     ] 
# )

urlpatterns = [
    path('', books, name='books'),
    path('api/', include(router.urls)),
]