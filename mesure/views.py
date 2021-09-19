from django.shortcuts import render
from datetime import datetime
from .models import mesure

date = datetime.now

# Create your views here.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        mesures=mesure.objects.filter(description__icontains=search)
    else:
        mesures=mesure.objects.all()

    return render(request, 'mesure/list.html', {'all':mesures,'date':date})
