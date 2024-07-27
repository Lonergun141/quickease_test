from django.urls import path, include
from .views import UploadFile
from .views import UserNotesCreateView, UserNotesDetailView, SummarizeText

urlpatterns = [
    path('list/', UploadFile, name='list'),
    
    #UserNotes
    path('usernotes/', UserNotesCreateView.as_view(), name='usernotes'),
    path('usernotes/<int:pk>/', UserNotesDetailView.as_view(), name='usernotes_detail'),
]
