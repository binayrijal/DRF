from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu =Student.objects.all()
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
    def update(self,request,pk=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'})
        return Response(serializer.errors)
    
    def partial_update(self,request,pk=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,partial=True,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'delete successfully'})
    
        

        
