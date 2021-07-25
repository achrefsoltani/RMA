from django.shortcuts import render, redirect
from datetime import datetime
from .forms import actifForm , typeActifForm , actifCritiqueForm
from .models import actif, typeActif , actifCritique

date = datetime.now

# Actif views.

def list(request):
    return render(request, 'actif/list.html', {'date':date})


def ajoutActif(request):

    form = actifForm()
    if request.method == 'POST':
        form = actifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listActifs')

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

# Type Actif views

def ajoutTypeActif(request):

    form = typeActifForm()
    if request.method == 'POST':
        form = typeActifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form}

    return render(request, "actif/type_actif_form.html", context)

def updateTypeActif(request, pk):
    type_pk = typeActif.objects.get(id=pk)

    form = typeActifForm(instance=type_pk)

    if request.method == 'POST':
        form = typeActifForm(request.POST, instance=type_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form}
    return render(request, "actif/type_actif_form.html", context)


# Actif Critique views

def ajoutActifCritique(request):

    form = actifCritiqueForm()
    if request.method == 'POST':
        form = actifCritiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form}

    return render(request, "actif/actif_critique_form.html", context)

def updateActifCritique(request, pk):
    critique_pk = actifCritique.objects.get(id=pk)

    form = actifCritiqueForm(instance=critique_pk)

    if request.method == 'POST':
        form = actifCritiqueForm(request.POST, instance=critique_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form}
    return render(request, "actif/actif_critique_form.html", context)
