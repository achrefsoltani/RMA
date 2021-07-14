from django.db import models

class TypeVulnerabilite(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)

    

class Vulnerabilite(models.Model):
   
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    #relations
      typeVulnerabilite = models.ForeignKey(TypeVulnerabilite, on_delete=models.SET_NULL)
      menace = models.ForeignKey(Menace, null=True, on_delete=models.SET_NULL)

     #logs
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
		    return self.type

class VulnerabiliteNote(models.Model):
    note = models.IntegerField()
    #relations
    actifCritique = models.ForeignKey(ActifCritique, on_delete=models.SET_NULL)
    vulnerabilite = models.ForeignKey(Vulnerabilite, on_delete=models.SET_NULL)

   







    


