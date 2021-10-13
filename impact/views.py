from django.shortcuts import render , redirect
from datetime import datetime
from .forms import impactForm , typeImpactForm, impactNoteForm
from .models import impact , typeImpact, impactNote
from .models import impact
from .models import typeImpact
from django.core.paginator import Paginator

date = datetime.now

# Impact views

def list(request):
    typeImpacts= typeImpact.objects.all()

    if 'search' in request.GET:
        search=request.GET['search']
        impacts=impact.objects.filter(description__icontains=search)
    else:    
        impacts= impact.objects.all()
      
    paginator= Paginator(impacts, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    return render(
        request, 
        'impact/list.html',
        {
            'all':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            'typeImpacts':  typeImpacts
        })

def ajoutImpact(request):

    form = impactForm(initial={'reference':'TLA'})
    if request.method == 'POST':
        form = impactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('listImpacts')

    context = {'form':form}

    return render(request, "impact/impact_form.html", context)


def updateImpact(request, pk):
    impact_pk = impact.objects.get(id=pk)

    form = impactForm(instance=impact_pk)

    if request.method == 'POST':
        form = impactForm(request.POST, instance=impact_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listImpacts')

    context = {'form':form}
    return render(request, "impact/impact_form.html", context)

def deleteImpact(request, pk):
    id = int(pk)
    try :
        impact_to_delete = impact.objects.get(id=id)
    except impact.DoesNotExist :
        return redirect('listImpacts')
    impact_to_delete.delete()
    return redirect('listImpacts')



# Type Impact views

def ajoutTypeImpact(request):

    form = typeImpactForm()
    if request.method == 'POST':
        form = typeImpactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listImpacts')

    context = {'form':form}

    return render(request, "impact/type_impact_form.html", context)

def updateTypeImpact(request, pk):
    type_pk = typeImpact.objects.get(id=pk)

    form = typeImpactForm(instance=type_pk)

    if request.method == 'POST':
        form = typeImpactForm(request.POST, instance=type_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listImpacts')

    context = {'form':form}
    return render(request, "impact/type_impact_form.html", context)


# Impact Noté views

def ajoutImpactNote(request):

    form = impactNoteForm()
    if request.method == 'POST':
        form = impactNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listImpacts')

    context = {'form':form}

    return render(request, "impact/impact_note_form.html", context)

def updateImpactNote(request, pk):
    note_pk = impactNote.objects.get(id=pk)

    form = impactNoteForm(instance=note_pk)

    if request.method == 'POST':
        form = impactNoteForm(request.POST, instance=note_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listImpacts')

    context = {'form':form}
    return render(request, "impact/impact_note_form.html", context)
