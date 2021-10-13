from django.shortcuts import redirect, render
from datetime import datetime

from actif.models import actif, actifCritique
from vulnerabilite.models import typeVulnerabilite, vulnerabilite, vulnerabiliteNote
from .models import session
from actif.models import actif, typeActif , actifCritique
from django.core.paginator import Paginator

date = datetime.now

# Session

def list(request , **args):

    sessions = session.objects.all()
  
    return render(request, 'session/list.html', {'sessions':sessions,'date':date})

def detail(request , **args):

    return render(request, 'session/detail.html', {'date':date})

def new(request , **args):
    new_session = session.objects.create(reference='testview')
    
    pk = new_session.id
    return redirect('choixAc', pk)

# Actifs Critiques
def choixAc(request , pk):
    typeactifs= typeActif.objects.all()
    
    if 'search' in request.GET:
        search=request.GET['search']
        actifs=actif.objects.filter(description__icontains=search)
    else:    
        actifs= actif.objects.all()
      
    paginator= Paginator(actifs, per_page=10)
    page_number= request.GET.get('page', 1)
    page_obj= paginator.get_page(page_number)
    
    current_session = session.objects.get(id=pk)
    try:
        ac_session = actifCritique.objects.filter(session__pk = current_session.id)
        a_session = [ac.actif for ac in ac_session]
    except:
        a_session = None
    
    return render(request, 'session/choixAc.html', {
            'all':page_obj.object_list,
            'paginator':paginator,
                'page_number': int(page_number),
            'typeactifs': typeactifs,
            'session': current_session,
            'actifsSession' : a_session
        })

def addAc(request , pk, pka):

    actifChoisi = actif.objects.get(id = pka)
    sessionEnCours = session.objects.get(id = pk)
    actifCritique.objects.create(session = sessionEnCours, actif = actifChoisi)
    return redirect('choixAc', pk)

def delAc(request , pk, pka):
    actifChoisi = actif.objects.get(id = pka)
    sessionEnCours = session.objects.get(id = pk)
    actifCritique.objects.filter(session = sessionEnCours, actif = actifChoisi).delete()
    return redirect('choixAc', pk)

def listAc(request , pk):
    current_session = session.objects.get(id=pk)
    try:
        ac_session = actifCritique.objects.filter(session__pk = pk)
        
    except:
        ac_session = None


    return render(request, 'session/listActifs.html', {'date':date, 'actifs':ac_session, 'session':current_session})

# Vulnérabilités Actif critique
def VulAc(request , pk):
    if request.method == 'POST' and request.POST.get('note').isdigit():
        
        desc =request.POST.get('desc')
        note =request.POST.get('note')
        vulChoisi = vulnerabilite.objects.filter(description = desc)
        print(vulChoisi)
        actifEnCours = actifCritique.objects.get(id = pk)
        vulnerabiliteNote.objects.create(vulnerabilite = vulChoisi[0], actif = actifEnCours, note=note)
            
    types = typeVulnerabilite.objects.all()
    vulnerabilites = vulnerabilite.objects.all()
    vulnerabilites_ac_note = vulnerabiliteNote.objects.filter(actif__pk = pk) 
    session_id = actifCritique.objects.filter(id=pk)[0].session.id
    return render(request, 'session/Vulnerabilites.html', {'date':date, 'pk':pk, "types":types, "vuls":vulnerabilites, "vulsAc" : vulnerabilites_ac_note, "id_session":session_id})


def delVul(request , pk, pkv):
    vulnerabiliteNote.objects.filter(id = pkv).delete()
    return redirect('VulAc', pk)

def MenAc(request , **args):

    return render(request, 'session/menaces.html', {'date':date})

def traitement(request , **args):

    return render(request, 'session/traitement.html', {'date':date})

def plan(request , **args):

    return render(request, 'session/rapport.html', {'date':date})




    
