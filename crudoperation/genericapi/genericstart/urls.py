from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.StudentGETPOSTAPI.as_view(),name="student"),
    path('student/<int:pk>/',views.StudentGETPOSTAPI.as_view(),name="student")
]