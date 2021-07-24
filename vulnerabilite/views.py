from django.shortcuts import render, redirect
from datetime import datetime
from .forms import vulnerabiliteForm
from .models import vulnerabilite

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


def updateVulnerabilite(request, pk):
    vulnerabilite_pk = vulnerabilite.objects.get(id=pk)

    form = vulnerabiliteForm(instance=vulnerabilite_pk)

    if request.method == 'POST':
        form = vulnerabiliteForm(request.POST, instance=vulnerabilite_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listVulnerabilites')

    context = {'form':form}
    return render(request, "vulnerabilite/vulnerabilite_form.html", context)