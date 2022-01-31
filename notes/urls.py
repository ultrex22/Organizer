"""organizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = 'Organizer Admin - Site Header'
admin.site.index_title = "Organizer - Index Title"

urlpatterns = [

    path('', views.NotesView.as_view(), name='notes'),
    path('detail/<slug:slug>', views.NoteDetailView.as_view(), name='note_detail'),
    path('new_note', views.NewNoteView,  name='new_note'),
    path('edit/<slug:slug>', views.EditNoteView.as_view(), name='edit_note'),
    path('delete_note/<slug:slug>', views.DeleteNoteView.as_view(), name='delete_note'),
]
