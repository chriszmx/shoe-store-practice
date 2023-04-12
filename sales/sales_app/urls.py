from django.urls import path
from .views import list_shoes, shoe_detail, cart_detail, cart_list


urlpatterns = [
    path('cart/<int:pk>', cart_detail, name='cart_detail'),
    path('cart/', cart_list, name='cart_list'),
    path('shoes/<int:pk>/', shoe_detail, name='shoe_detail'),
    path('shoes/', list_shoes, name='list_shoes'),
]
