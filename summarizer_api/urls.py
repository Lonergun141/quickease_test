from django.urls import path, include
from .views import UploadFile

urlpatterns = [
    path('list/', UploadFile, name='list')
]
