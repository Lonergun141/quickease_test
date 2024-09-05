from django.contrib import admin
from .models import UserTest, TestQuestion, TestChoices, ChoiceAnswer
# Register your models here.

admin.site.register(UserTest)
admin.site.register(TestQuestion)
admin.site.register(TestChoices)
admin.site.register(ChoiceAnswer)
