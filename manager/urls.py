from django.urls import path
from .views import *


urlpatterns = [
    #manager  urls
    path('create_admin/', create_admin , name="create_client"),
    path('get_admin_id/', get_admin_by_id, name="delete_client_id"),
    path('get_admin_email/', get_admin_by_email, name="get_cleint_email"),



    # path('/update/<str:id>', update_client, name="update_client"),
]
