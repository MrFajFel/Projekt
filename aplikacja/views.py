from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from aplikacja.models import Notatka
from django.views.generic import ListView



# Create your views here.
# def note_list(request):
#     notes = Notatka.objects.all()
#     return render(request, "post/list.html",{"notes":notes})
# Create your views here.
class NoteListView(ListView):
    queryset = Notatka.objects.all().filter(status='published')
    context_object_name = 'notes'
    paginate_by = 3
    template_name = "post/list.html"


def note_detail(request, year, month, day):
    note = get_object_or_404(Notatka,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, "post/detail.html",
                  {'note': note,})