from rest_framework import serializers
from .models import *

class resturantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resturant
        fields="__all__"

class barserializer(serializers.ModelSerializer):
    class Meta:
        model=bar
        fields="__all__"

class inverntorySerializer(serializers.ModelSerializer):
    class Meta:
        model=inverntory
        fields="__all__"

class laundrySerializer(serializers.ModelSerializer):
    class Meta:
        model=laundry
        fields="__all__"