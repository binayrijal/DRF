from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.StudentAPI.as_view(),name="student"),
    path('student/<int:pk>',views.StudentAPI.as_view(),name="student")
]