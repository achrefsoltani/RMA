from django.db import models

class Session(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    debut= models.DateField()
    fin= models.DateField()
    statut = models.CharField(max_length=150)
    #clé table actif critique
    actifCritique =  models.CharField(max_length=150)
    planTraitement = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


