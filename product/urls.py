from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_product, name="create_product"),
    path('get', get_product, name="get_product"),
    path('delete', delete_product, name="delete_product"),
    path('update', update_product, name="update_product")
]
