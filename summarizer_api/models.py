from django.db import models
from django.utils.translation import gettext_lazy as _ 
# Create your models here.

class UserNotes(models.Model):
    notetitle = models.CharField(_("Note Title"), max_length=30)
    notecontents = models.TextField(_("Note Contents"))
    notedatecreated = models.DateTimeField(auto_now_add=True)