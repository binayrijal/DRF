from django.urls import path
from . import views

urlpatterns=[
    path('view_student/',views.view_student,name="view_student")
]