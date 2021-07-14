from django.db import models
from actif.models import ActifCritique

class TypeImpact(models.Model):
    reference = models.CharField(max_length=150, null=True)
    description= models.TextField(blank=True, null=True)
     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Impact(models.Model):
    description= models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=150, null=True)
    impactFaible = models.CharField(max_length=150, null=True)
    impactMoyen = models.CharField(max_length=150, null=True)
    impactFort = models.CharField(max_length=150, null=True)
    #relations
    typeImpact = models.ForeignKey(TypeImpact, null=True, on_delete=models.SET_NULL)
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
		    return self.categorie

class ImpactNote(models.Model):
    NoteImpact= models.IntegerField(null=True)
    NoteOcc= models.IntegerField(null=True)
    #relations
    actifCritique = models.ForeignKey(ActifCritique, null=True, on_delete=models.SET_NULL)
    impact = models.ForeignKey(Impact, null=True, on_delete=models.SET_NULL)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)








