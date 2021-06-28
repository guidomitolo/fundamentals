from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import viewsets_generic as views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('books/',
        views.BooksList.as_view(),
        name='book-list'),
    path('books/<int:pk>/',
        views.BooksDetail.as_view(),
        name='book-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])