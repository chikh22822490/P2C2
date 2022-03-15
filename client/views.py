from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import *
from .selectors import *
from .services import *


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def create_client(request):
    data =  request.data
    client_data =  data['client']
    user = Account.objects.create(
        email=data["email"],
        name=data["name"],
        password =  data['password'],
        is_active=True,
        is_staff=False
    )
    if isinstance(user, Account):
        client = Client(user=user, first_name=client_data['first_name'],
                        last_name=client_data['last_name'], telephone=client_data['telephone'])
        client.save()
        serializer = ClientSerializers(client, many=False)
        return Response(serializer.data)
    return  Response({"error" :  "the client didn't add"})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_clients(request):
    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        clients = None
    if clients:
        print(clients)
        serialiszer = ClientSerializers(clients, many=True)
        return Response(serialiszer.data)
    return Response({"error": "there is no clients in the Database"})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_client_by_id(request):
    data = request.data
    id = data['id']
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        client = None
    if client:
        serialiszer = ClientSerializers(client, many=False)
        return Response(serialiszer.data)
    return {"error": "there is no clients in the Database"}





@api_view(['GET'])
@permission_classes([AllowAny])
def get_client_by_email(request):
    data = request.data
    email = data['email']
    try:
        client = Client.objects.get(email =  email)
    except Client.DoesNotExist:
        client = None
    if client:
        serialiszer = ClientSerializers(client, many=False)
        return Response(serialiszer.data)
    return {"error": "there is no clients in the Database"}

