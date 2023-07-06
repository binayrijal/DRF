from django.urls import path
from . import views

urlpatterns=[
    path('viewserial/<int:pk>',views.serial,name="serial"),
    path('viewdeserial/',views.deserial,name="deserial")
]