from django.shortcuts import render
from serial.models import Student
from serial.serializer import StudentSerializer,StudentDeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from django.http import JsonResponse



# Create your views here.
def serial(request,pk):
    stu=Student.objects.get(id=pk)
    complex_item=StudentSerializer(stu)
    json_data=JSONRenderer().render(complex_item.data)

    return HttpResponse(json_data,content_type='application/json')



@csrf_exempt
def deserial(request):
 if request.method=='POST':
    json_data=request.body
    stream=io.BytesIO(json_data)
    pythondata=JSONParser.parse(stream)
    deserializedata=StudentDeSerializer(data=pythondata)
    if deserializedata.is_valid():
       Student.save()
       res={'msg':'data is save'}
       json_data=JSONRenderer().render(res)
       return HttpResponse(json_data,content_type='application/json')
    
    error={'msg':'data is not valid'}
    json_data=JSONRenderer().render(error) 
    return HttpResponse(json_data,content_type='application/json')
