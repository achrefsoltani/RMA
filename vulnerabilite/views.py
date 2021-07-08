from django.shortcuts import render
from datetime import datetime

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'vulnerabilite/list.html', {'date':date})