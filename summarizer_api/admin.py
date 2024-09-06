from django.contrib import admin
from .models import UserNotes

# Register your models here.

class UserNotesAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    readonly_fields = ['notetitle', 'notecontents', 'notedatecreated', 'notesummary']

    def show_package_delivery_pattern(self, obj):
        if obj.notetitle:
            return obj.notetitle
        else:
            return 'N/A'

admin.site.register(UserNotes, UserNotesAdmin)