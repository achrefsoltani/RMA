from django.shortcuts import redirect, render
from datetime import datetime

from actif.models import actif, actifCritique
from menace.models import menace
from mesure.models import mesure
from vulnerabilite.models import typeVulnerabilite, vulnerabilite, vulnerabiliteNote
from .models import session
from actif.models import actif, typeActif , actifCritique
from impact.models import impact, impactNote
from django.core.paginator import Paginator

date = datetime.now

# Session

def list(request , **args):

    sessions = session.objects.all()
  
    return render(request, 'session/list.html', {'sessions':sessions,'date':date})

def detail(request , **args):

    return render(request, 'session/detail.html', {'date':date})

def new(request , **args):
    new_session = session.objects.create()
    new_session.reference = 'S'+ str(new_session.id) + '/' + str(new_session.debut.year)
    new_session.description = 'Session '+ str(new_session.debut.year)
    new_session.statut = 'En cours'
    new_session.save()
    
    pk = new_session.id
    return redirect('choixAc', pk)

def delSess(request , pk):
    session.objects.filter(id=pk).delete()
    return redirect('listSessions')

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

def finAc(request,pk, pka):
    actifC = actifCritique.objects.filter(id = pka).first()
    actifC.etat = 'Fini'
    actifC.save()
    return redirect('listAc', pk)
# Vulnérabilités Actif critique
def VulAc(request , pk):
    if request.method == 'POST' and request.POST.get('note').isdigit():
        
        desc =request.POST.get('desc')
        note =request.POST.get('note')
        vulChoisi = vulnerabilite.objects.filter(description = desc)
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

# Menaces Actif critique
def MenAc(request , pk):

    impacts = impact.objects.all()
    actifEnCours = actifCritique.objects.get(id = pk)
    pks = actifEnCours.session.id
    
    if request.method == 'POST' and request.POST.get('note').isdigit() and request.POST.get('occurence').isdigit():
        access = request.POST.get('access')
        acteur = request.POST.get('acteur')
        motivation = request.POST.get('motivation')
        resultat = request.POST.get('resultat')
        impactChoisi = request.POST.get('impact')
        
        impactc = impact.objects.filter(description=impactChoisi).first()
        
        note = request.POST.get('note')
        occurence = request.POST.get('occurence')
        menaceCree = menace.objects.create(access=access,acteur=acteur,motivation=motivation,resultat=resultat,actif=actifEnCours)
        menaceCree.reference = 'M'+ str(menaceCree.id)
        menaceCree.save()
        impactNote.objects.create(menace=menaceCree, note_impact=note, note_occurence=occurence, impact=impactc)
        

    menaceActif = menace.objects.filter(actif=actifEnCours)
    impactsadded =[]
    for m in menaceActif:
        impactsadded.append(impactNote.objects.filter(menace=m).first())

    return render(request, 'session/menaces.html', {'date':date, 'impacts':impacts, 'impactsAdded':impactsadded, 'pka':pk,'pks':pks})

def delMen(pks, pki):
    
    impactNote.objects.filter(id=pki).delete()    
    return redirect('MenAc', pks)

# Session  

def traitement(request , pk):

    
    ac_session = actifCritique.objects.filter(session__pk = pk)
    L =[]
    for a in ac_session:
        Maturite = 0
        NoteVul = 0
        NoteImp = 0
        Occurence = 0
        ag = a.actif
        acs = actifCritique.objects.filter(actif_id=ag.id)
        for ac in acs :
            mesures = mesure.objects.filter(actif_critique = ac.id)
            for m in mesures:
                Maturite += m.note
                
        vuls = vulnerabiliteNote.objects.filter(actif_id = a.id)
        for v in vuls:
            NoteVul += v.note
            
        menaces = menace.objects.filter(actif_id = a.id)
        for me in menaces:
            imp = impactNote.objects.filter(menace_id = me.id).first()
            NoteImp += imp.note_impact
            Occurence += imp.note_occurence
        
        Risque = (NoteVul * Occurence * NoteImp) - Maturite
        a.incidents = Occurence
        a.maturite = Maturite
        a.note_risque = Risque
        a.save()
        L.append([a,NoteVul,Occurence,NoteImp,Maturite,Risque])


    return render(request, 'session/traitement.html', {'date':date, 'items':L, 'pk':pk})

def addMes(request,pk, pka):
    if request.method == 'POST' and request.POST.get('note').isdigit():
        a = actifCritique.objects.filter(id=pka)
        m = mesure.objects.create(type = request.POST.get('traitement'), description = request.POST.get('traitement'), etat ='en cours', note = request.POST.get('note'), actif_critique =a )
        m.reference = 'M'+ str(m.id)
    return redirect('traitement',pk)
def plan(request , **args):

    return render(request, 'session/rapport.html', {'date':date})




    
