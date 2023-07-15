from .serializer import StudentSerializer
from rest_framework.views import APIView
from .models import Student
from rest_framework.response import Response


class StudentAPI(APIView):
    
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
         stu=Student.objects.get(id=id)
         serializer=StudentSerializer(stu)
         return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
       data=request.data
       print(data)
       serializer=StudentSerializer(data=data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'data created'})
       
    def patch(self,request,pk,format=None):
       id=pk
       data=request.data
       stu=Student.objects.get(id=id)
       serializer=StudentSerializer(stu,partial=True,data=data)
       if serializer.is_valid():
         serializer.save()
         return Response({'msg':'data updated partilly'})
    
       return Response(serializer.errors)
    def put(self,request,pk,format=None):
       id=pk
       data=request.data
       stu=Student.objects.get(id=id)
       serializer=StudentSerializer(stu,data=data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'data update complete'})
       return Response(serializer.errors)
    def delete(self,request,pk):
       id=pk
       stu=Student.objects.get(id=id)
       stu.delete()
       return Response({'msg':'delete successfully'})
