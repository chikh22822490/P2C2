from rest_framework.serializers import ModelSerializer
from .models import *



class PCSerializers(ModelSerializer):
    class Meta:
        model = PointCollection
        fields = '__all__'