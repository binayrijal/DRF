from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer