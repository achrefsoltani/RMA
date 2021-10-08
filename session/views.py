from django.shortcuts import render
from datetime import datetime
from .models import session

date = datetime.now

# Create your views here.

def list(request , **args):

    return render(request, 'session/list.html', {'date':date})

def detail(request , **args):

    return render(request, 'session/detail.html', {'date':date})

def choix(request, **args):

    return render(request, 'session/choix.html', {'date':date})
    
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
    
