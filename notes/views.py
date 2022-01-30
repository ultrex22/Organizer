from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, View
from django.utils.text import slugify
from django.urls import reverse

from .forms import AllNotesForm
from .models import Notes

all_notes = Notes.objects.all().order_by('-date')


def home(request):
    return render(request, 'index.html')


class NotesView(ListView):
    queryset = all_notes
    template_name = 'all_notes.html'


def NewNoteView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AllNotesForm(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_note = form.save(commit=False)
            new_note.slug = slugify(request.POST['title'])
            new_note.save()
            return HttpResponseRedirect(reverse('notes'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AllNotesForm()

    return render(request, 'new_note.html', {'form': form})


class NoteDetailView(View):

    def get(self, request, slug):
        single_note = Notes.objects.get(slug=slug)
        context = {"single_note": single_note}
        return render(request, 'note_detail.html', context)


class EditNoteView(UpdateView):
    model = Notes
    context_object_name = 'note'
    fields = ['title', 'text', 'color', 'image']
    template_name = 'edit_note.html'
    success_url = '/notes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteNoteView(DeleteView):
    model = Notes
    context_object_name = 'note'
    fields = ['title', 'text', 'color', 'image']
    template_name = 'delete_note.html'
    success_url = '/notes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

