from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class typeActif(models.Model):

    reference = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class actif(models.Model):
    
    reference = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    criticite_affaire = models.IntegerField()
    cid = models.IntegerField()
    proprietaire = models.CharField(max_length=50)
    
    #Relationships

    # type = typeActif
    #actifs_en_relation = liste d'actifs
    #mesures_existantes = liste de mesures

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class actifCritique(models.Model):

    incidents = models.IntegerField()
    maturite = models.IntegerField()
    note_risque = models.IntegerField()

    #Relationships

    #actif
    #session
    #vulnerabilite
    #menaces
    #impacts
    #traitement

     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    