from django.shortcuts import render

import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *
# Create your views here.





# Create your views here.
@api_view(["GET"])
def get_panier(request):
    try:
        farmer = Panier.objects.all()
    except farmer.DoesNotExist:
        farmer = None
    serializer = PanierSerializer(farmer, many=True)
    return Response(serializer.data)
