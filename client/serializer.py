from rest_framework.serializers import ModelSerializer
from .models import *



class ClientSerializers(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'