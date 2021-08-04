from django.shortcuts import render
from datetime import datetime
from .models import actifCritique

date = datetime.now

# Create your views here.

def list(request):
    actifs= actifCritique.objects.all()
    return render(request, 'actif/list.html', {'date':date},{'all':actifs})