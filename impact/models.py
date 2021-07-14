from django.db import models

class TypeImpact(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
     #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Impact(models.Model):
    description= models.TextField(blank=True)
    reference = models.CharField(max_length=150)
    impactFaible = models.CharField(max_length=150)
    impactMoyen = models.CharField(max_length=150)
    impactFort = models.CharField(max_length=150)
    #relations
    typeImpact = models.CharField(max_length=150)
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
		    return self.categorie

class ImpactNote(models.Model):
    NoteImpact= models.IntegerField()
    NoteOcc= models.IntegerField()
    #relations
    actifCritique = models.CharField(max_length=150)
    impact = models.CharField(max_length=150)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)








