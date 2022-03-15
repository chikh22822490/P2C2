from rest_framework.serializers import ModelSerializer
from .models import *

class DeliveryManSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'