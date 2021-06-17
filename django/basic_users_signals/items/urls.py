from django.urls import path
from items import views

urlpatterns = [
    path('stock/', views.stock, name='stock'),
    path('order/', views.order, name='order'),
]