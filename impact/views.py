from django.shortcuts import render
from datetime import datetime
from .models import impact

date = datetime.now

# Create your views here.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        all_impacts=impact.objects.filter(description__icontains=search)
    else:
        all_impacts= impact.objects.all()
    return render(request, 'impact/list.html', {'all':all_impacts})