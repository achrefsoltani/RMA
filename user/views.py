from django.shortcuts import render
from datetime import datetime

date = datetime.now

# Create your views here.

def profile(request):
    return render(request, 'user/profile.html', {'date':date})