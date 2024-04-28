from django.http import HttpResponse
from django.shortcuts import render

from aplikacja.models import Notatka


# Create your views here.
def note_list(request):
    notes = Notatka.objects.all()
    return render(request, "post/list.html",{"notes":notes})
# Create your views here.
