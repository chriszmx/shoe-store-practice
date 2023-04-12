from django.urls import path
from .views import show_customer, list_customers


urlpatterns = [
    path('customer/<int:pk>/', show_customer, name='show_customer'),
    path('customers/', list_customers, name='list_customers'),
]
