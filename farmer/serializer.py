from rest_framework.serializers import ModelSerializer
from .models import *

class farmerSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'