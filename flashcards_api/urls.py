from django.urls import path
from .views import UserFlashcardsListView, CreateFlashcardsView, EditFlashcardView, AddFlashcardView, DeleteFlashcardView

urlpatterns = [
    path('user-flashcards/<int:user_id>/', UserFlashcardsListView.as_view(), name='user_flashcards'),
    path('create-flashcards/<int:note_id>/', CreateFlashcardsView.as_view(), name='create_flashcards'),
    path('edit-flashcard/<int:flashcard_id>/', EditFlashcardView.as_view(), name='edit_flashcard'),
    path('add-flashcard/<int:note_id>/', AddFlashcardView.as_view(), name='add_flashcard'),
    path('delete-flashcard/<int:flashcard_id>/', DeleteFlashcardView.as_view(), name='delete_flashcard'),
    
]
