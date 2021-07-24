from django.shortcuts import render, redirect
from datetime import datetime
from .forms import actifForm

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'actif/list.html', {'date':date})


def ajoutActif(request):

    form = actifForm()
    if request.method == 'POST':
        form = actifForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, "actif/actif_form.html", context)
    