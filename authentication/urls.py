from django.urls import path
from .views import *


urlpatterns = [
    # les urls des devis appartment
    #post
    path('create/', create_client , name="create_client"),
    path('delete/', delete_client, name="delete_client"),
    #get
    path('get_clients/', get_clients, name="get_all_clients"),
    path('get_client/', get_client, name="get_one_client"),
    path('get_client_by_email/', get_client_email,  name="get_client_by_email"),

    # path('/update/<str:id>', update_client, name="update_client"),
]
