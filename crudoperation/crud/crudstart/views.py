from django.shortcuts import render,redirect
import io
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerialzer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

# Create your views here.
def view_student(request):
    if request.method=='GET':
        form_data=request.body
        stream=io.BytesIO(form_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerialzer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerialzer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
