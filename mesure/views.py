from django.shortcuts import render
from datetime import datetime
from .models import mesure
from django.core.paginator import Paginator

date = datetime.now

# Create your views here.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        mesures=mesure.objects.filter(description__icontains=search)
    else:
        mesures=mesure.objects.all()

    paginator= Paginator(mesures, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    return render(
        request, 
        'mesure/list.html',
        {
            'all':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            
        })
