from django.shortcuts import render , redirect
from datetime import datetime
from .forms import impactForm , typeImpactForm, impactNoteForm
from .models import impact , typeImpact, impactNote

date = datetime.now

# Impact views

def list(request):
    return render(request, 'impact/list.html', {'date':date})


def ajoutImpact(request):

    form = impactForm()
    if request.method == 'POST':
        form = impactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

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
