from rest_framework import serializers
from .models import UserTest, TestQuestion, TestChoices, ChoiceAnswer

class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFlashCards
        fields = "__all__"

class TestQuestionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = "__all__"
        
class TestChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestChoices
        fields = "__all__"
        
class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = "__all__"
        
