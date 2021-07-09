from django.db import models

class Menace(models.Model):
    type = models.CharField(max_length=150)
    reference = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    acces = models.CharField(max_length=150)
    acteur = models.CharField(max_length=150)
    motivation = models.CharField(max_length=150)
    resultat = models.CharField(max_length=150)

    def __str__(self):
		    return self.type
