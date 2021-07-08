from django.shortcuts import render
from datetime import datetime

date = datetime.now

# Create your views here.

def home(request):
    return render(request, 'root/home.html', {'date':date})