from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'obj created succesfully'})
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu)
        return Response(serializer.data)

    
        

        
