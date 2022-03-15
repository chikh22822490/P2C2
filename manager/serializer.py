from rest_framework.serializers import ModelSerializer
from .models import *



class AdminSerializers(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'