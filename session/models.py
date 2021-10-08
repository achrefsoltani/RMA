from django.db import models

# Create your models here.

class session(models.Model):

    reference = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    debut = models.DateTimeField(null=True)
    fin = models.DateTimeField(null=True)
    statut = models.CharField(max_length=50, null=True)

    #Relationships


    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = .....

    def __str__(self):
        return self.reference