from django.db import models
from django.utils.translation import gettext_lazy as _ 
from .text_summarizer import summarize
from users.models import User
from .title_generator import generate_title

# Create your models here.

class UserNotes(models.Model):
    notetitle = models.CharField(_("Note Title"), max_length=30)
    notecontents = models.TextField(_("Note Contents"))
    notedatecreated = models.DateTimeField(auto_now_add=True)
    notesummary = models.TextField(_("Note Summary"), blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    class Meta: 
        verbose_name = _("User Note")
        verbose_name_plural = _("User Notes")
    
    def save(self, *args, **kwargs):
        if not self.notetitle:  
            self.notetitle = generate_title(
                paragraph=self.notecontents
                )
        super(UserNotes, self).save(*args, **kwargs)
        
        if not self.notesummary:  
            self.notesummary = summarize(
                text=self.notecontents,
                detail=1, 
                model='gpt-4o-mini',
                additional_instructions="Provide a concise summary of the content."
            )
        super(UserNotes, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.notetitle