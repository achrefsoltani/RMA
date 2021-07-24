from django.shortcuts import render, redirect
from datetime import datetime
from .forms import mesureForm

date = datetime.now

# Create your views here.

def list(request):
    return render(request, 'mesure/list.html', {'date':date})


def ajoutMesure(request):

    form = mesureForm()
    if request.method == 'POST':
        form = mesureForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, "mesure/mesure_form.html", context)