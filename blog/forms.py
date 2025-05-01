from django import forms
from .models import WorldCup
class WorldCupForm(forms.ModelForm):
    class Meta:
        model = WorldCup
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar Mundial', max_length=100)
