from rest_framework import serializers
from myapp.models import *

class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = "__all__"

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = "__all__"

class CreateElevatorRequestSerializer(serializers.ModelSerializer):
    requested_floors = serializers.ListField(child=serializers.IntegerField())
    class Meta:
        model = ElevatorRequest
        fields = ["current_floor","requested_floors"]

class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = "__all__"


