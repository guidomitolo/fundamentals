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
from django.urls import path

from users import views as user_views
from main import views as main_views

from django.contrib.auth import views as log_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # home view (without include -> there is no urls.py in views/ app)
    path('home/', main_views.home, name='home'),
    # register view
    path('register/', user_views.register, name='register'),
    # login default view function
    path('login/', log_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # logout default view function
    path('logout/', log_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
