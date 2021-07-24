from django import forms
from django.forms import ModelForm, widgets
from .models import mesure


class mesureForm(ModelForm):
    
    class Meta:
        model = mesure
        fields = '__all__'