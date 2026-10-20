from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Programme

def liste_programmes(request):
    programmes = Programme.objects.filter(actif=True)
    return render(request, 'programmes/liste.html', {'programmes': programmes})

def detail_programme(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    return render(request, 'programmes/detail.html', {'programme': programme})