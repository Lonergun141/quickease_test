from django.shortcuts import render
from rest_framework import viewsets
from .models import Pomodoro
from .serializers import PomodoroSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PomodoroViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pomodoro.objects.filter(user=user)