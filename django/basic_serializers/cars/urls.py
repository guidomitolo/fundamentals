from django.urls import path, include

from cars.views import cars, django_serializer, django_serializer_2, rest_framework_model_viewset 
from cars.views import rest_framework_api_view_list, rest_framework_api_view_detail, rest_framework_api_view_create, rest_framework_api_view_update, rest_framework_api_view_delete

from rest_framework import routers

# rather than explicitly registering the views in a viewset in the urlconf, 
# you'll register the viewset with a router class, 
# that automatically determines the urlconf for you.
router = routers.DefaultRouter()
router.register("rest_framework_model_viewset", rest_framework_model_viewset)

urlpatterns = [
    path('', cars, name='cars'),
    # django simple api
    path('simplest_api', django_serializer, name='simplest_api'),
    path('simplest_api_2', django_serializer_2, name='simplest_api_2'),
    # django rest framework view
    path('rest_framework_api_view_list', rest_framework_api_view_list, name='rest_framework_api_view_list'),
    path('rest_framework_api_view_detail/<str:pk>', rest_framework_api_view_detail, name='rest_framework_api_view_detail'),
    path('rest_framework_api_view_create', rest_framework_api_view_create, name='rest_framework_api_view_create'),
    path('rest_framework_api_view_update/<str:pk>', rest_framework_api_view_update, name='rest_framework_api_view_update'),
    path('rest_framework_api_view_delete/<str:pk>', rest_framework_api_view_delete, name='rest_framework_api_view_delete'),
    path('', include(router.urls)),
]