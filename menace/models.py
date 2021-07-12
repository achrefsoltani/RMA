from django.db import models

# Create your models here.

class menace(models.Model):

    type = models.CharField(max_length=50, null=True)
    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    access = models.CharField(max_length=50, null=True)
    acteur = models.CharField(max_length=50, null=True)
    motivation = models.CharField(max_length=50, null=True)
    resultat = models.CharField(max_length=50, null=True)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.description