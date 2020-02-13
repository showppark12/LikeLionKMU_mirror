from .models import *
from rest_framework import serializers

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields  = '__all__'


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'