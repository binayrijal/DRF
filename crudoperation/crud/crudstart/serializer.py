from .models import Student
from rest_framework import serializers


class StudentSerialzer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)