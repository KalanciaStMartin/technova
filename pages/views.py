from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def accueil(request):
    return render(request, 'pages/accueil.html')

def a_propos(request):
    return render(request, 'pages/a_propos.html')

def contact(request):
    return render(request, 'pages/contact.html')