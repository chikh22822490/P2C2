from rest_framework.serializers import ModelSerializer
from .models import *

class PanierSerializer(ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'