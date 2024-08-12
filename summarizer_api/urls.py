from django.urls import path, include
from .views import UploadFile
from .views import UserNotesListCreateView, UserNotesRetrieveUpdateDestroyView

urlpatterns = [
    path('list/', UploadFile, name='list'),
    
    #UserNotes
    path('summarizer/usernotes/', UserNotesListCreateView.as_view(), name='usernotes-list'),
    path('summarizer/usernotes/<int:pk>/', UserNotesRetrieveUpdateDestroyView.as_view(), name='usernotes_detail-retrieve-update-destroy'),
]
