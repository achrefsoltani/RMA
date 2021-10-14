from django.db import models

from actif.models import actifCritique

# Create your models here.

class menace(models.Model):

    CHOICES = (
        ('HR','Acteur Humain & Access réseau'),
        ('HP','Acteur Humain & Access physique'),
        ('PS','Problèmes systèmes'),
        ('AP','Autres Problèmes')

    )

    type = models.CharField(max_length=50, choices= CHOICES ,null=True)
    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    access = models.CharField(max_length=50, null=True)
    acteur = models.CharField(max_length=50, null=True)
    motivation = models.CharField(max_length=50, null=True)
    resultat = models.CharField(max_length=50, null=True)

    #Relationships

    actif = models.ForeignKey(actifCritique, null=True, on_delete=models.SET_NULL)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return str(self.id)