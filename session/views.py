from django.shortcuts import render
from datetime import datetime

from actif.models import actif, actifCritique
from .models import session

date = datetime.now

# Create your views here.

def list(request , **args):

    sessions = session.objects.all()
    return render(request, 'session/list.html', {'sessions':sessions,'date':date})

def detail(request , **args):

    return render(request, 'session/detail.html', {'date':date})

def choix(request):
    new_id = 3
    s = session.objects.create(reference ='S2021'+str(new_id),description="Session "+str(new_id))
    actifs = actif.objects.all()
    return render(request, 'session/choix.html', {'date':date, 'actifs':actifs})

def ajoutActifC(request,a):
    ac = actifCritique.objects.create(actif=a)
    return render(request, 'session/choix.html', {'date':date, 'actifs':actifs})
    
def listActifC(request, **args):

    return render(request, 'session/listActifs.html', {'date':date})
    
def vulnerabilites(request, **args):

    return render(request, 'session/Vulnerabilites.html', {'date':date})
    
def menaces(request, **args):

    return render(request, 'session/menaces.html', {'date':date})
    
def traitement(request, **args):

    return render(request, 'session/traitement.html', {'date':date})
    
def rapport(request, **args):

    return render(request, 'session/rapport.html', {'date':date})


    
