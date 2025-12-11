from .models import Programme

def programmes_context(request):
    return {
        'programmes': Programme.objects.filter(actif=True).order_by('ordre')
    }
