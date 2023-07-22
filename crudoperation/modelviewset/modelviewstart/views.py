from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    """this is authentication and permission which is inside class we need to write.
    IF we want to appy for all the class .here we have two class StudentModelViewSet and StudentReadOnlyViewSet so we add 
     REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated'],
     } in setting.py """
    
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]

class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer