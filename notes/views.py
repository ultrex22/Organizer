from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from .forms import AllNotesForm
from .models import Notes


def home(request):
    return render(request, 'index.html')


all_notes = Notes.objects.all().order_by('-date')


class AllNotesView(ListView):
    queryset = Notes.objects.all()
    template_name = 'all_notes.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['text_sample'] = "sample"
    #     return context


class NoteDetailView(DetailView):
    def get(self, request):
        # more logic here#
        return render(request, 'note_detail.html')


class EditNoteView(UpdateView):
    def get(self, request):
        # more logic
        return render(request, 'edit_note.html')

    # class NewNoteView(FormView):
    #     def get(self, request):
    #         return render(request, 'new_note.html')


def NewNoteView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AllNotesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AllNotesForm()

    return render(request, 'new_note.html', {'form': form})


class DeleteNoteView(DeleteView):
    def get(self, request):
        return render(request, 'delete_note.html')

    def post(self, request):
        pass
