from django.db import models

class TypeActif(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
class Actif(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    criticiteAffaire = models.IntegerField()
    cid = models.IntegerField()
    proprietaire = models.CharField(max_length=150)
    #relation
    typeActif = models.ForeignKey(TypeActif, on_delete=models.SET_NULL)
    actifRelation = models.ForeignKey(Actif, null=True, on_delete=models.SET_NULL)
    
     #logs
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
class ActifCritique(models.Model):
    IncidentsPasse = models.IntegerField()
    maturite = models.IntegerField()
    noteRisque = models.IntegerField()
    #relation
    actif = models.CharField(max_length=150)
    session = models.CharField(max_length=150)

          



