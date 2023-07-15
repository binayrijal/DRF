from .serializer import StudentSerializer
from rest_framework.views import APIView
from .models import Student
from rest_framework.response import Response


class StudentAPI(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
         stu=Student.objects.get(id=id)
         serializer=StudentSerializer(stu)
         return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request,format=None,):
       data=request.data
       print(data)
       serializer=StudentSerializer(data=data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'data created'})
       

