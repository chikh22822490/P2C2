from rest_framework.serializers import ModelSerializer
from .models import *

class farmerSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'