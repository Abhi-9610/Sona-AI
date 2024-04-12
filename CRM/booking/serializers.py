from rest_framework import serializers
from .models import *
class bookingserializer(serializers.ModelSerializer):
    class Meta:
        model=Bookingdetails
        fields="__all__"