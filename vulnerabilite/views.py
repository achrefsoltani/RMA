from django.shortcuts import render
from datetime import datetime
from .models import vulnerabilite
from .models import typeVulnerabilite

date = datetime.now

# Create your views here.

def list(request):

    vulnerabilites = vulnerabilite.objects.all()
    typesVulnerabilites =  typeVulnerabilite.objects.all()
                               
    return render(request, 'vulnerabilite/list.html', {'all':vulnerabilites, 'allType':typesVulnerabilites})