from django.shortcuts import render , redirect
from datetime import datetime
from .forms import impactForm
from .models import impact

date = datetime.now

# Create your views here.

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