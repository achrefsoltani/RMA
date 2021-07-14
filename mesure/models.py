from django.db import models

class Mesure(models.Model):
    reference = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    etat= models.TextField(blank=True)
    dateImplementation = models.DateTimeField()
    note = models.IntegerField()
    #relations
    actifCritique = models.CharField(max_length=150)
     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

