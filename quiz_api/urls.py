from django.urls import path
from .views import UserTestListView, CreateTestView

urlpatterns = [
    path('user_tests/', UserTestListView.as_view(), name='user-test-view'),
    path('quiz_api/v1/createtest/<int:note_id>/', CreateTestView.as_view(), name='create-test-view'),
]
