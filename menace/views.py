from django.shortcuts import render, redirect
from datetime import datetime
from .forms import menaceForm

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'menace/list.html', {'date':date})


def ajoutMenace(request):

    form = menaceForm()
    if request.method == 'POST':
        form = menaceForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, "menace/menace_form.html", context)