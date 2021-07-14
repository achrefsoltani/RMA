from django.db import models
from actif.models import actif, actifCritique

# Create your models here.

class mesure(models.Model):

    reference = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    etat = models.CharField(max_length=50, null=True)
    note = models.IntegerField(null=True)

    #Relationships

    actif_critique = models.OneToOneField(actifCritique, null=True, on_delete=models.SET_NULL)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return  self.description

