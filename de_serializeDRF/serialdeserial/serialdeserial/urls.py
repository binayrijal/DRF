
from django.contrib import admin
from django.urls import path,include
from serial.views import deserial,serial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('serial/',include('serial.urls')),
    path('deserial/',include('serial.urls'))
]
