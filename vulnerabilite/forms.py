from django import forms
from django.forms import ModelForm, widgets
from .models import vulnerabilite, typeVulnerabilite, vulnerabiliteNote


class vulnerabiliteForm(ModelForm):
    
    class Meta:
        model = vulnerabilite
        fields = '__all__'


class typeVulnerabiliteForm(ModelForm):

    class Meta:
        model = typeVulnerabilite
        fields ='__all__'


class vulnerabiliteNoteForm(ModelForm):

    class Meta:
        model = vulnerabiliteNote
        fields = '__all__'