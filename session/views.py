from django.shortcuts import render
from datetime import datetime
from .models import session

date = datetime.now

# Create your views here.

def list(request):
    all_sessions= session.objects.all()
    return render(request, 'session/list.html', {'date':date},{'all':all_sessions})