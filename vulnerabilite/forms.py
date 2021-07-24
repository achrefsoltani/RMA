from django import forms
from django.forms import ModelForm, widgets
from .models import vulnerabilite


class vulnerabiliteForm(ModelForm):
    
    class Meta:
        model = vulnerabilite
        fields = '__all__'