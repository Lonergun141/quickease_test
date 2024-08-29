from django.db import models
from django.utils.translation import gettext_lazy as _ 
from .text_summarizer import summarize
from users.models import User

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
        if not self.notesummary:  
            self.notesummary = summarize(
                text=self.notecontents,
                detail=1, 
                model='gpt-4o-mini',
               additional_instructions=(
                "As a professional summarizer, create a concise and comprehensive summary of the provided text, "
                "be it an article, post, conversation, or passage, while adhering to these guidelines:\n\n"
                "Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.\n\n"
                "Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.\n\n"
                "Rely strictly on the provided text, without including external information.\n\n"
                "Format the summary in paragraph form for easy understanding.\n\n"
                "In other words, include a message counter where you start with #1 and add 1 to the message counter every time I send a message.\n\n"
                "By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner."
                )
            )
        super(UserNotes, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.notetitle