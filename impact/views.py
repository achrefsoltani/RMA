from django.shortcuts import render
from datetime import datetime
from .models import impact
from .models import typeImpact
from django.core.paginator import Paginator

date = datetime.now

# Create your views here.

def list(request):
    typeImpacts= typeImpact.objects.all()

    if 'search' in request.GET:
        search=request.GET['search']
        impacts=impact.objects.filter(description__icontains=search)
    else:    
        impacts= impact.objects.all()
      
    paginator= Paginator(impacts, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    return render(
        request, 
        'impact/list.html',
        {
            'all':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            'typeImpacts':  typeImpacts
        })