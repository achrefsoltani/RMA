from actif.models import actifCritique
from django.db import models
from menace.models import menace


# Create your models here.

class typeImpact(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description


class  impact(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    faible = models.CharField(max_length=50, null=True)
    moyen = models.CharField(max_length=50, null=True)
    fort = models.CharField(max_length=50, null=True)

    #Relationships

    type = models.ForeignKey(typeImpact, null=True, on_delete=models.SET_NULL)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description

class impactNote(models.Model):

    note_impact = models.IntegerField(null=True)
    note_occurence = models.IntegerField(null=True)

    #Relationships

    impact = models.ForeignKey(impact, null=True, on_delete=models.SET_NULL)

    menace = models.OneToOneField(
        menace,
        on_delete=models.CASCADE,
        null=True
    )

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    