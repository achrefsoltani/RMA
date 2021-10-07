from django.shortcuts import render, redirect
from datetime import datetime
from .forms import ACform, actifForm , typeActifForm , actifCritiqueForm
from .models import actif, typeActif , actifCritique
from .models import actifCritique
from .models import actif
from .filters import ActifFilter
from django.core.paginator import Paginator

date = datetime.now

# Actif views.

def list(request):
    if 'search' in request.GET:
        search=request.GET['search']
        actifs=actif.objects.filter(description__icontains=search)
    else:    
        actifs= actif.objects.all()
      
    paginator= Paginator(actifs, per_page=3)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    return render(
        request, 
        'actif/list.html',
        {
            'all':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number)
        }
    )


def ajoutActif(request):

    form = actifForm()
    form2 = ACform()
    if request.method == 'POST':
        form = actifForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('listActifs')

    context = {'form':form , 'form2': form2}

    return render(request, "actif/actif_form.html", context)

def updateActif(request, pk):
    actif_pk = actif.objects.get(id=pk)
    actifs_critiques = actifCritique.objects.filter(actif = actif_pk)
    form = actifForm(instance=actif_pk)

    if request.method == 'POST':
        form = actifForm(request.POST, instance=actif_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listActifs')

    context = {'form':form, 'actifs':actif_pk.actifs_en_relations.all(), 'actifC': actifs_critiques.all()}
    return render(request, "actif/actif_form.html", context)

def deleteActif(request, pk):
    id = int(pk)
    try :
        actif_to_delete = actif.objects.get(id=id)
    except actif.DoesNotExist :
        return redirect('listActifs')
    actif_to_delete.delete()
    return redirect('listActifs')

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
    
