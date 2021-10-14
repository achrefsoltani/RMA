from django.db import models
from session.models import session

# Create your models here.

class typeActif(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class actif(models.Model):
    
    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    criticite_affaire = models.IntegerField(null=True)
    cid = models.IntegerField(null=True)
    proprietaire = models.CharField(max_length=50, null=True)
    intervenant = models.CharField(max_length=50, null=True)
    #Relationships

    type = models.ForeignKey(typeActif, null=True, on_delete=models.SET_NULL)
    actifs_en_relations = models.ManyToManyField('self', blank=True, null=True, symmetrical=True)
    

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return str(self.id)


class actifCritique(models.Model):

    incidents = models.IntegerField(null=True)
    maturite = models.IntegerField(null=True)
    note_risque = models.IntegerField(null=True)
    etat = models.CharField(max_length=50, null=True)
    #Relationships

    actif = models.ForeignKey(actif, null=True, on_delete=models.SET_NULL)
    session = models.ForeignKey(session, null=True, on_delete=models.SET_NULL) 
    

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return str(self.id)

    