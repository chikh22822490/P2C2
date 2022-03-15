from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_delivrer, name="create_delivrer"),
    path('get', get_delivrer, name="get_delivrer"),
    path('delete', delete_delivrer, name="delete_delivrer"),
    path('update', update_delivrer, name="update_delivrer")
]