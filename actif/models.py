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
     typeActif = models.CharField(max_length=150)
     actifRelation = models.CharField(max_length=150)
     mesure = models.CharField(max_length=150)
     #logs
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)



