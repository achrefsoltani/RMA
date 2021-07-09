from django.db import models

class CategorieImpact(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)



class Impact(models.Model):
    #clé table categorie impact
    categorie = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    reference = models.CharField(max_length=150)
    impactFaible = models.CharField(max_length=150)
    impactMoyen = models.CharField(max_length=150)
    impactFort = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
		    return self.categorie

class ImpactNote(models.Model):
    #clé table actif
    actif = models.CharField(max_length=150)
    NoteImpact= models.IntegerField()
    NoteOcc= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







