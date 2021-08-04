from django.shortcuts import render
from datetime import datetime
from .models import impact

date = datetime.now

# Create your views here.

def list(request):
    all_impacts= impact.objects.all()
    return render(request, 'impact/list.html', {'date':date},{'all':all_impacts})