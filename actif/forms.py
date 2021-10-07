from django import forms
from django.forms import ModelForm, fields, widgets
from .models import actif, actifCritique, typeActif


class actifForm(ModelForm):
    
    class Meta:
        model = actif
        fields = [
            'reference',
            'description',
            'criticite_affaire',
            'cid',
            'proprietaire',
            'intervenant',
            
        ]


class typeActifForm(ModelForm):
    class Meta:
        model = typeActif
        fields = '__all__'



class actifCritiqueForm(ModelForm):
    class Meta:
        model = actifCritique
        fields = '__all__'
       

class ACform(forms.Form):
    reference = forms.CharField(max_length=50)