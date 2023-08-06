from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import StudentSerializer
from .models import Student
from .mypagination import MyPageNumberPagination



# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination
    