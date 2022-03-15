from django.shortcuts import render

# Create your views here.
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *

# Create your views here.
@api_view(["GET"])
def get_farmer(request):
    try:
        farmer = Farmer.objects.all()
    except farmer.DoesNotExist:
        farmer = None
    serializer = farmerSerializer(farmer, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_farmer(request):
    data = request.data
    time.sleep(1)
    print("this is id :  ", id)
    
    farmer = Farmer.objects.create(
        firstNameFarmer = data['firstNameFarmer'],
        lastNameFarmer = data['lastNameFarmer'],
        phoneFarmer = data['phoneFarmer'],
        emailFarmer= data['emailFarmer'],
        adressFarmer= data['adressFarmer']
    )
    serializer = farmerSerializer(farmer)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["PUT"])
def update_farmer(request): 
    data = request.data
    farmer = Farmer.objects.get(id=request.data['id'])
    serializer = farmerSerializer(instance=farmer, data=data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def delete_farmer(request):
    farmer = Farmer.objects.get(id=request.data['id'])
    farmer.delete()
    return Response("Farmer was deleted")