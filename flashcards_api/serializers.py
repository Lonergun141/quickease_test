from rest_framework import serializers
from .models import UserFlashCards

class UserFlashCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFlashCards
        fields = '__all__'