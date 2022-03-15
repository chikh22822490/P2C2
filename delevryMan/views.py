import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *

# Create your views here.

@api_view(["GET"])
def get_delivrer(request):
    try:
        delivrer = DeliveryMan.objects.all()
    except delivrer.DoesNotExist:
        delivrer = None
    serializer = DeliveryManSerializer(delivrer, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_delivrer(request):
    data = request.data
    time.sleep(1)
    print("this is id :  ", id)
    
    delivrer = DeliveryMan.objects.create(
        firstNameDeliverer = data['firstNameDeliverer'],
        lastNameDeliverer = data['lastNameDeliverer'],
        phoneDeliverer = data['phoneDeliverer'],
        emailDeliverer= data['emailDeliverer']
    )
    serializer = DeliveryManSerializer(delivrer)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["PUT"])
def update_delivrer(request): 
    data = request.data
    delivrer = DeliveryMan.objects.get(id=request.data['id'])
    serializer = DeliveryManSerializer(instance=delivrer, data=data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def delete_delivrer(request):
    delivrer = DeliveryMan.objects.get(id=request.data['id'])
    delivrer.delete()
    return Response("Delivery man was deleted")