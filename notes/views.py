from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')


def notes(request):
    return render(request, 'notes.html')


def note_detail(request):
    return render(request, 'note_detail.html')


def edit_note(request):
    return render(request, 'edit_note.html')


def new_note(request):
    return render(request, 'new_note.html')
