from django.db.models import fields
from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer
from .models import Cottage, Room


class CottageSerializer(ModelSerializer):
    class Meta:
        model = Cottage
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'