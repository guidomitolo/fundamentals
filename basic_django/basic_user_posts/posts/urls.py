from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# path + view function + name to call from the template
urlpatterns = [

    # to view a VIEW OBJECT -> OBJECT + as_view() method
    path('', PostListView.as_view(), name='home'),


    # url reference = <app>/<model>_<viewype>.html

    # VIEW OBJECT + VARIABLE (pk = primary key) in route
    # RENDERING DEFAULT in post_detail/post_form/post_confirm_delete.html
    # name = <app>-detail/create/update/delete
    # int require to change/update post to avoid intrusions

    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('posts/new/', PostCreateView.as_view(), name='post-create'),

    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),

    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]