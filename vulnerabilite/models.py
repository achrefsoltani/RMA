from django.db import models

class TypeVulnerabilite(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)

    

class Vulnerabilite(models.Model):
    #clé table typeVulnerabilite
    type = models.CharField(max_length=150)
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    #clé table menace
    menace = models.CharField(max_length=150)

    def __str__(self):
		    return self.type

class VulnerabiliteNote(models.Model):
    #clé table actif critique
    actif = models.CharField(max_length=150)
    note = models.IntegerField()







    


