from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student



# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def helloworld(request,pk=None):
  if request.method=="GET":
    id=pk
    if id is not None:
     stu=Student.objects.get(id=id)
     serializer=StudentSerializer(stu)
     return Response(serializer.data)
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return Response(serializer.data)

  if request.method=="POST": 
    print(request.data)
    return Response({'msg':'this is post method','data':request.data})
  if request.method=="PUT":
    return Response({'msg':'hellow this is put'})
  if request.method=="PATCH":
    return Response({'msg':'hellow this is patch'})
  if request.method=="DELETE":
    return Response({'msg':'hellow this is delete'})
