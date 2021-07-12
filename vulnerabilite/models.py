from django.db import models
from menace.models import menace
from actif.models import actifCritique

# Create your models here.

class typeVulnerabilite(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class vulnerabilite(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)

    #Relationships

    type = models.ForeignKey(typeVulnerabilite, null=True, on_delete=models.SET_NULL)
    menace = models.ForeignKey(menace, null=True, on_delete=models.SET_NULL)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class vulnerabiliteNote(models.Model):

    note = models.IntegerField(null=True)

    #Relationships

    vulnerabilite = models.ForeignKey(vulnerabilite, null=True, on_delete=models.SET_NULL)
    actif = models.ForeignKey(actifCritique, null=True, on_delete=models.SET_NULL)
