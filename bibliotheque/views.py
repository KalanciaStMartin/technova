from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Ressource

def index(request):
    ressources = Ressource.objects.all()
    return render(request, 'bibliotheque/index.html', {'ressources': ressources})