import django_filters
from .models import *

class ActifFilter(django_filters.FilterSet):
    class Meta:
        model = actif
        fields = '__all__'