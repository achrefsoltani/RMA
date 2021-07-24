from django.shortcuts import render, redirect
from datetime import datetime
from .forms import actifForm
from .models import actif

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'actif/list.html', {'date':date})


def ajoutActif(request):

    form = actifForm()
    if request.method == 'POST':
        form = actifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, "actif/actif_form.html", context)

def updateActif(request, pk):
    actif_pk = actif.objects.get(id=pk)

    form = actifForm(instance=actif_pk)

    if request.method == 'POST':
        form = actifForm(request.POST, instance=actif_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form}
    return render(request, "actif/actif_form.html", context)