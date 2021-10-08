from actif import models
from django import forms
from django.forms import ModelForm, fields, widgets
from .models import impact, typeImpact, impactNote


class impactForm(ModelForm):
    
    class Meta:
        model = impact
        fields = [
            'reference',
            'description',
            'faible',
            'moyen',
            'fort',    
        ]



class typeImpactForm(ModelForm):

    class Meta:
        model = typeImpact
        fields ='__all__'


class impactNoteForm(ModelForm):

    class Meta:
        model = impactNote
        fields = '__all__'