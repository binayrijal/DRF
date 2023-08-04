from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from modelviewstart.customauth import CustomAuth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

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
    #this is basic authetication

    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]

    #this is session authentication
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

class StudentReadOnlyViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    #this is for how many times you want to access api 
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

class Studentfilter(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(user)