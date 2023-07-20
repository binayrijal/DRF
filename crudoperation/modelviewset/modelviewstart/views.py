from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]

class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer