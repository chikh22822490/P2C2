from django.shortcuts import render
from user.models import Account
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializer import *


# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def get_admin_by_id(request):
    data = request.data
    print(data)
    try:
        admin = Admin.objects.get(id=data['id'])
    except Admin.DoesNotExist:
        admin = None
    if admin:
        serializer = AdminSerializers(admin, many=False)
        return Response(serializer.data)
    return Response({"Error": "There is not  Admin  with  this id"})


@api_view(["GET"])
@permission_classes([AllowAny])
def get_admin_by_email(request):
    data = request.data
    try:
        admin = Admin.objects.get(email=data['email'])
    except Admin.DoesNotExist:
        admin = None
    if admin:
        serializer = AdminSerializers(admin, many=False)
        return Response(serializer.data)
    return Response({"Error": "There is not  Admin  with  this email"})


@api_view(["POST"])
@permission_classes([AllowAny])
def create_admin(request):
    data = request.data
    if Account.objects.filter(email=data["email"]).exists():
        return Response({"error": "the user already existe"})
    user = Account.objects.create(
        email=data["email"],
        name=data["name"],
        password=data['password'],
        is_active=True,
        is_staff=False
    )
    admin = Admin.objects.create(user=user, last_name=data['last_name'], first_name=data['first_name'],
                                 telephone=data['telephone'], email=data['email'])
    if isinstance(admin, Admin):
        return Response({"success": "the manager  is added successefully"})
    return Response({"error": "he manager  has not be added"})
