from django.db import models
from session.models import Session

class TypeActif(models.Model):
    reference = models.CharField(max_length=150, null=True)
    description= models.TextField(blank=True, null=True)
class Actif(models.Model):
    reference = models.CharField(max_length=150, null=True)
    description= models.TextField(blank=True, null=True)
    criticiteAffaire = models.IntegerField(null=True)
    cid = models.IntegerField(null=True)
    proprietaire = models.CharField(max_length=150, null=True)
    #relation
    typeActif = models.ForeignKey(TypeActif, null=True, on_delete=models.SET_NULL)
    actifRelation = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    
     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class ActifCritique(models.Model):
    IncidentsPasse = models.IntegerField(null=True)
    maturite = models.IntegerField(null=True)
    noteRisque = models.IntegerField(null=True)
    #relation
    actif = models.ForeignKey(Actif, null=True, on_delete=models.SET_NULL)
    session = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)

          



