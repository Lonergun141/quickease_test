from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class Pomodoro(models.Model):
    study_time = models.PositiveIntegerField(default=25)
    short_break = models.PositiveIntegerField(default=5)
    long_break = models.PositiveIntegerField(default=15)
    show_timer = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = _("Pomodoro")
        verbose_name_plural = _("Pomodoro")