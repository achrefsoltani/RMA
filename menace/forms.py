from django import forms
from django.forms import ModelForm, widgets
from .models import menace


class menaceForm(ModelForm):
    
    class Meta:
        model = menace
        fields = '__all__'