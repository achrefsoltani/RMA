from django.db import models

class TypeVulnerabilite(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)

    

class Vulnerabilite(models.Model):
   
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    #relations
     type = models.CharField(max_length=150)
     menace = models.CharField(max_length=150)

     #logs
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
		    return self.type

class VulnerabiliteNote(models.Model):
    note = models.IntegerField()
    #relations
    actifCritique = models.CharField(max_length=150)
    vulnérabilite = models.CharField(max_length=150)

   







    


