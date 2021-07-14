from django.db import models
from actif.models import ActifCritique

class Mesure(models.Model):
    reference = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    etat= models.TextField(blank=True)
    dateImplementation = models.DateTimeField()
    note = models.IntegerField()
    #relations
    actifCritique = models.ForeignKey(ActifCritique, null=True, on_delete=models.SET_NULL)
     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

