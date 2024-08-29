from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserFlashCards
from summarizer_api.models import UserNotes
from .serializers import UserNotesSerializer, UserFlashCardsSerializer
import json
from rest_framework.permissions import IsAuthenticated
from .flashcards import generate_flashcards

class UserFlashcardsListView(generics.ListAPIView):
    serializer_class = UserFlashCardsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserFlashCards.objects.filter(noteID__user=user)

class NoteFlashcardsListView(generics.ListAPIView):
    serializer_class = UserFlashCardsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        note_id = self.kwargs['note_id']
        user = self.request.user
        return UserFlashCards.objects.filter(noteID_id=note_id, noteID__user=user)

class CreateFlashcardsView(APIView):
    def post(self, request, note_id):
        note = generics.get_object_or_404(UserNotes, id=note_id)
        paragraph = note.notesummary

        if not paragraph:
            return Response({"status": "error", "message": "Note summary is empty."}, status=status.HTTP_400_BAD_REQUEST)

        JSON_DATA = generate_flashcards(paragraph)
        

        try:
            flashcards_data = json.loads(JSON_DATA)
            flashcards_list = []
            
            for flashcard in flashcards_data:
                front = flashcard.get('Front', '')
                back = flashcard.get('Back', '')
                
                flashcard_instance = UserFlashCards.objects.create(
                    noteID=note,
                    frontCardText=front,
                    backCardText=back
                )
                flashcards_list.append(UserFlashCardsSerializer(flashcard_instance).data)
                
            return Response({"status": "success", "flashcards": flashcards_list}, status=status.HTTP_201_CREATED)
        
        except json.JSONDecodeError:
            return Response({"status": "error", "message": "Failed to decode JSON response."}, status=status.HTTP_400_BAD_REQUEST)

class EditFlashcardView(APIView):
    def put(self, request, flashcard_id):
        flashcard = generics.get_object_or_404(UserFlashCards, id=flashcard_id)
        serializer = UserFlashCardsSerializer(flashcard, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "flashcard": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddFlashcardView(APIView):
    def post(self, request, note_id):
        note = generics.get_object_or_404(UserNotes, id=note_id)
        serializer = UserFlashCardsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(noteID=note)
            return Response({"status": "success", "flashcard": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteFlashcardView(APIView):
    def delete(self, request, flashcard_id):
        flashcard = generics.get_object_or_404(UserFlashCards, id=flashcard_id)
        flashcard.delete()
        return Response({"status": "success", "message": "Flashcard deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
