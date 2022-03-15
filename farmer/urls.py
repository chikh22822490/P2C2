from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_farmer, name="create_farmer"),
    path('get', get_farmer, name="get_farmer"),
    path('delete', delete_farmer, name="delete_farmer"),
    path('update', update_farmer, name="update_farmer")
]
