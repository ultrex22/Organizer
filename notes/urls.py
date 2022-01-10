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

from django.urls import path

from . import views

urlpatterns = [

    path('', views.notes, name='notes'),
    path('detail/', views.note_detail, name='note_detail'),
    path('edit/', views.edit_note, name='edit_note'),
]
