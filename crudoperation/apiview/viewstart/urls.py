from django.urls import path
from . import views

urlpatterns=[
    path('student/<int:pk>',views.helloworld,name="helloworld"),
]