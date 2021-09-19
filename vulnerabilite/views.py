from django.shortcuts import render
from datetime import datetime
from .models import vulnerabilite
from .models import typeVulnerabilite

date = datetime.now

# Create your views here.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        vulnerabilites=vulnerabilite.objects.filter(description__icontains=search)
    else:
        vulnerabilites = vulnerabilite.objects.all()
    typesVulnerabilites =  typeVulnerabilite.objects.all()   
                               
    return render(request, 'vulnerabilite/list.html', {'all':vulnerabilites, 'allType':typesVulnerabilites})