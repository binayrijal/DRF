from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.helloworld,name="helloworld"),
    path('student/<int:pk>',views.helloworld,name="helloworld"),
]