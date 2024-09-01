from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserNotes
from .serializers import UserNotesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def UploadImage(request):
    pass

#User Notes

class UserNotesListCreateView(generics.ListCreateAPIView):
    serializer_class = UserNotesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserNotes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class UserNotesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserNotesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserNotes.objects.filter(user=self.request.user)
