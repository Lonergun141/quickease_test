from django.db import models
from django.utils.translation import gettext_lazy as _ 
# Create your models here.

class UserNotes(models.Model):
    notetitle = models.CharField(_("Note Title"), max_length=30)
    notecontents = models.TextField(_("Note Contents"))
    notedatecreated = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.notesummary:  
            self.notesummary = summarize(
                text=self.notecontents,
                detail=0.5, 
                model='gpt-4o-mini',
                additional_instructions="Provide a concise summary of the content."
            )
        super(UserNotes, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.notetitle