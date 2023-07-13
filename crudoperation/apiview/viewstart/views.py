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
    data=request.data
    serializer=StudentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'data save'})
    
    return Response({'msg':'this is post method','data':request.data})
    
  if request.method=="PUT":

    id=pk
    stu=Student.objects.get(id=id)
    serializer=StudentSerializer(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'put method completed'})

    return Response({'msg':'hellow this is put without valid'})
  
  if request.method=="PATCH":
    id=pk
    stu=Student.objects.get(id=id)
    serializer=StudentSerializer(stu,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'patch method completed'})

    return Response({'msg':'hellow this is patch without valid'})
  if request.method=="DELETE":
    id=pk
    stu=Student.objects.get(id=id)
    stu.delete()
    return Response({'msg':'hellow this is delete'})
