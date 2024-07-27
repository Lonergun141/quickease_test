from rest_framework import serializers
from .models import UserNotes

class UserNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotes
        fields = '__all__'