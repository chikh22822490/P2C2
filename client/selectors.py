'''
from django.db.models.query import QuerySet
from .models import Client


def get_clients() -> QuerySet[Client]:
    qs = Client.objects.all()
    return qs'''

from django.db.models.query import QuerySet
from django.apps import apps

Client = apps.get_model('client', 'Client')


def verify_client(id) -> bool:
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return False
    return True


def get_all() -> QuerySet[Client]:
    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        clients = None
    return clients


def get_Client(id) -> Client:
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        client = None
    return client


def get_Client_By_Email(email) -> Client:
    try:
        client = Client.objects.get(email=email)
    except Client.DoesNotExist:
        return {"error": "there is no client by that email "}
    return client
