from django.shortcuts import render
from datetime import datetime
from .models import actifCritique
from .models import actif
from .models import typeActif
from .filters import ActifFilter
from django.core.paginator import Paginator

date = datetime.now

# Create your views here.

def list(request):
    typeactifs= typeActif.objects.all()
    if 'search' in request.GET:
        search=request.GET['search']
        actifs=actif.objects.filter(description__icontains=search)
    else:    
        actifs= actif.objects.all()
      
    paginator= Paginator(actifs, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    return render(
        request, 
        'actif/list.html',
        {
            'all':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            'typeactifs': typeactifs
        })

def listByType(request):  
    actifsByTypes= actif.objects.all()

    return render(
        request, 
        'actif/listByType.html',
        {
            
         'actifsByTypes': actifsByTypes
        }
    )