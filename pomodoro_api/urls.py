from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PomodoroViewSet

router = DefaultRouter()
router.register(r'', PomodoroViewSet, basename='pomodoro')

urlpatterns = [
    path('pomodoro_api/v1/', include(router.urls)),
]
