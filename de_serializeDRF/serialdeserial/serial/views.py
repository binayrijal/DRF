from django.shortcuts import render
from serial.models import Student
from serial.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student



# Create your views here.
def serial(request):
    stu=Student.objects.get(id=1)
    complex_item=StudentSerializer(stu)
    json_data=JSONRenderer().render(complex_item.data)

    return HttpResponse(json_data,content_type='application/json')