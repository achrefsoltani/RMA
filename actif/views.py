from django.shortcuts import render
from datetime import datetime
from .models import actifCritique
from .models import actif
from .filters import ActifFilter

date = datetime.now

# Create your views here.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        actifs=actif.objects.filter(description__icontains=search)
    else:    
        actifs= actif.objects.all()
    
    
    
    return render(request, 'actif/list.html', {'all':actifs})