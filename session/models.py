from django.db import models

class Session(models.Model):
    reference = models.CharField(max_length=150)
    description= models.TextField(blank=True)
    debut= models.DateField()
    fin= models.DateField()
    statut = models.CharField(max_length=150)
    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


