from django import forms
from django.forms import ModelForm, widgets
from .models import impact


class impactForm(ModelForm):
    
    class Meta:
        model = impact
        fields = '__all__'