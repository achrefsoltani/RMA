from django import forms
from django.forms import ModelForm, widgets
from .models import actif


class actifForm(ModelForm):
    
    class Meta:
        model = actif
        fields = [
            'reference',
            'description',
            'criticite_affaire',
            'cid',
            'proprietaire',
            'type',
            'actifs_en_relations'
        ]

        