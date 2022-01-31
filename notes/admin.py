from django.contrib import admin

from .models import Notes


# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    site_header = 'Ultimate Organizer'
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'text', 'color', 'image')
    list_display = ('title', 'text', 'color', 'image')


admin.site.register(Notes, NotesAdmin)
