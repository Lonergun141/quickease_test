from rest_framework import serializers
from .models import UserFlashCards
from summarizer_api.models import UserNotes

class UserNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotes
        fields = ['id', 'notetitle', 'notecontents', 'notesummary', 'user', 'notedatecreated']

class UserFlashCardsSerializer(serializers.ModelSerializer):
    note_title = serializers.CharField(source='noteID.notetitle', read_only=True)
    class Meta:
        model = UserFlashCards
        fields = '__all__'