from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserTest, TestQuestion, TestChoices
from summarizer_api.models import UserNotes
from .serializers import UserTestSerializer, TestQuestionSerializer, TestChoicesSerializer
import json
from rest_framework.permissions import IsAuthenticated
from .question_create import generate_questions
from .choice_create import generate_choices

# Generic Views
class UserTestListView(generics.ListAPIView):
    serializer_class = UserTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserTest.objects.filter(note__user=user)

# Create Test
class CreateTestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, note_id):
        note = generics.get_object_or_404(UserNotes, id=note_id)
        usertest = generics.get_object_or_404(UserTest, note_id=note_id)
        paragraph = note.notesummary

        if not paragraph:
            return Response({"status": "error", "message": "Note summary is empty."}, status=status.HTTP_400_BAD_REQUEST)
        
        

        JSON_DATA = generate_questions(paragraph)

        try:
            question_data = json.loads(JSON_DATA)
            question_list = []

            for item in question_data:
                question_text = item.get('Question', '')

                question_instance = TestQuestion.objects.create(
                    test=usertest,
                    TestQuestion=question_text
                )
                question_list.append(TestQuestionSerializer(question_instance).data)

                try:
                    question_choices_data = generate_choices(question_text)
                    choice_list = []

                    for choice in question_choices_data:
                        choice_a = choice.get('choice', '')
                        isanswer = choice.get('isAnswer', False)

                        choice_instance = TestChoices.objects.create(
                            question=question_instance,  # Use the question_instance, not the raw question text
                            item_choice_text=choice_a,
                            isAnswer=isanswer
                        )
                        choice_list.append(TestChoicesSerializer(choice_instance).data)

                except json.JSONDecodeError:
                    return Response({"status": "error", "message": "Failed to decode JSON response for choices."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": "success", "questions": question_list}, status=status.HTTP_201_CREATED)

        except json.JSONDecodeError:
            return Response({"status": "error", "message": "Failed to decode JSON response for questions."}, status=status.HTTP_400_BAD_REQUEST)
