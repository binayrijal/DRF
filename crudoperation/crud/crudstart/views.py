from django.shortcuts import render,redirect
import io
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
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
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method=='POST':
        form_data=request.body
        stream=io.BytesIO(form_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data is created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        