"""basic_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import home
from houses.views_REST import houses_detail, houses_list, houses
from houses.viewsets_REST import houses_list as houses_list_class
from houses.viewsets_REST import houses_detail as houses_detail_class


urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', home, name='home'),
    # cars urls
    path('cars/', include('cars.urls')),
    # houses db+api
    path('houses/', houses, name='houses'),
    # REST Framwork views/templates requires url declaration
    # path('houses/api', houses_list, name='houses_api'),
    path('houses/api', houses_list_class.as_view()),
    # path('houses/api/<int:pk>', houses_detail),
    path('houses/api/<int:pk>', houses_detail_class.as_view()),
] 

