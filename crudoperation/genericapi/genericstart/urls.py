from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.StudentGETPOSTAPI.as_view(),name="student"),
    path('student/<int:pk>/',views. StudentUPDATEDELETE.as_view(),name="student"),
    path('apistudent/',views.StudentGETPOSTAPI.as_view()),
    path('apistudent/<int:pk>/',views. StudentUPDATEDELETE.as_view(),name="student"),
]