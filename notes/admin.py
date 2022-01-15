from django.contrib import admin

from .models import Notes


# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    site_header = 'Ultimate Organizer'


admin.site.register(Notes, NotesAdmin)
