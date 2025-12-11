from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Evenement

def liste_evenements(request):
    evenements = Evenement.objects.filter(archive=False)
    return render(request, 'evenements/liste.html', {'evenements': evenements})