from django.shortcuts import render, redirect
from datetime import datetime
from .forms import vulnerabiliteForm

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'vulnerabilite/list.html', {'date':date})



def ajoutVulnerabilite(request):

    form = vulnerabiliteForm()
    if request.method == 'POST':
        form = vulnerabiliteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, "vulnerabilite/vulnerabilite_form.html", context)