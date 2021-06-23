from django.urls import path, include

from cars.views import cars, simplest_api, simplest_api_2, simplest_api_4, simplest_api_3_list, simplest_api_3_detail, simplest_api_3_create, simplest_api_3_update, simplest_api_3_delete

from rest_framework import routers

# rather than explicitly registering the views in a viewset in the urlconf, 
# you'll register the viewset with a router class, 
# that automatically determines the urlconf for you.
router = routers.DefaultRouter()
router.register("simplest_api_4", simplest_api_4)

urlpatterns = [
    path('', cars, name='cars'),
    path('simplest_api', simplest_api, name='simplest_api'),
    path('simplest_api_2', simplest_api_2, name='simplest_api_2'),
    path('simplest_api_3_list', simplest_api_3_list, name='simplest_api_3_list'),
    path('simplest_api_3_detail/<str:pk>', simplest_api_3_detail, name='simplest_api_3_detail'),
    path('simplest_api_3_create', simplest_api_3_create, name='simplest_api_3_create'),
    path('simplest_api_3_update/<str:pk>', simplest_api_3_update, name='simplest_api_3_update'),
    path('simplest_api_3_delete/<str:pk>', simplest_api_3_delete, name='simplest_api_3_delete'),
    path('', include(router.urls)),
]