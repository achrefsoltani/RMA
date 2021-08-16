from django.shortcuts import render
from datetime import datetime
from .models import actifCritique
from .models import actif
from pprint import pprint

date = datetime.now

# Create your views here.

def list(request):
    actifs= actif.objects.all()
    
    
    return render(request, 'actif/list.html', {'all':actifs})