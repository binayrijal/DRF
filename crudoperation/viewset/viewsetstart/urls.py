from django.urls import path,include
from .models import Student
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r'student',views.StudentViewSet,basename='student')

urlpatterns=[
    path('',include(router.urls))
]