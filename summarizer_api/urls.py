from django.urls import path, include
from .views import UserNotesListCreateView, UserNotesRetrieveUpdateDestroyView

urlpatterns = [
    
    
    #UserNotes
    path('usernotes/', UserNotesListCreateView.as_view(), name='usernotes-list'),
    path('usernotes/<int:pk>/', UserNotesRetrieveUpdateDestroyView.as_view(), name='usernotes_detail-retrieve-update-destroy'),
]
