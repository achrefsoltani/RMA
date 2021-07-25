from django.shortcuts import render, redirect
from datetime import datetime
from .forms import vulnerabiliteForm, typeVulnerabiliteForm, vulnerabiliteNoteForm
from .models import vulnerabilite , typeVulnerabilite , vulnerabiliteNote

date = datetime.now

# Vulnerabilite views

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


# Type Vulnerabilite views

def ajoutTypeVulnerabilite(request):

    form = typeVulnerabiliteForm()
    if request.method == 'POST':
        form = typeVulnerabiliteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listVulnerabilites')

    context = {'form':form}

    return render(request, "vulnerabilite/type_vulnerabilite_form.html", context)

def updateTypeVulnerabilite(request, pk):
    type_pk = typeVulnerabilite.objects.get(id=pk)

    form = typeVulnerabiliteForm(instance=type_pk)

    if request.method == 'POST':
        form = typeVulnerabiliteForm(request.POST, instance=type_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listVulnerabilites')

    context = {'form':form}
    return render(request, "vulnerabilite/type_vulnerabilite_form.html", context)


# Vulnerabilite noté views

def ajoutVulnerabiliteNote(request):

    form = vulnerabiliteNoteForm()
    if request.method == 'POST':
        form = vulnerabiliteNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listVulnerabilites')

    context = {'form':form}

    return render(request, "vulnerabilite/vulnerabilite_note_form.html", context)

def updateVulnerabiliteNote(request, pk):
    note_pk = vulnerabiliteNote.objects.get(id=pk)

    form = vulnerabiliteNoteForm(instance=note_pk)

    if request.method == 'POST':
        form = vulnerabiliteNoteForm(request.POST, instance=note_pk)
        
        if form.is_valid():
            form.save()
            return redirect('listVulnerabilite')

    context = {'form':form}
    return render(request, "vulnerabilite/vulnerabilite_note_form.html", context)


