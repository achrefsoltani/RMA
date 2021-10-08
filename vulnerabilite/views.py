from django.shortcuts import render
from datetime import datetime
from .models import vulnerabilite
from .models import typeVulnerabilite
from django.core.paginator import Paginator

date = datetime.now

# Create your views here.

def list(request):
    typesVulnerabilites =  typeVulnerabilite.objects.all()   
    if 'search' in request.GET:
        search=request.GET['search']
        vulnerabilites=vulnerabilite.objects.filter(description__icontains=search)
    else:
        vulnerabilites = vulnerabilite.objects.all()
    paginator= Paginator(vulnerabilites, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
                               
    return render(request, 'vulnerabilite/list.html', { 'allType':typesVulnerabilites,
        'all':page_obj.object_list,
        'paginator':paginator,
        'page_number': int(page_number),
    })