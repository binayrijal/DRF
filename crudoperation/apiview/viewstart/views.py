from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def helloworld(request):
  if request.method=="GET":
    return Response({'msg':'hello world'})

  if request.method=="POST": 
    print(request.data)
    return Response({'msg':'this is post method','data':request.data})
  if request.method=="PUT":
    return Response({'msg':'hellow this is put'})
  if request.method=="PATCH":
    return Response({'msg':'hellow this is patch'})
  if request.method=="DELETE":
    return Response({'msg':'hellow this is delete'})
