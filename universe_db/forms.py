from django import forms
from dal import autocomplete
from .models import SolarSystemPlanets, PlanetarySystems

class PlanetForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=SolarSystemPlanets.objects.all(),
        widget=autocomplete.ModelSelect2(url='universe_db:planet-autocomplete')
    )

    class Meta:
        model = SolarSystemPlanets
        fields = ['name',]


class PlanetarySystemForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=PlanetarySystems.objects.all(),
        widget=autocomplete.ModelSelect2(url='universe_db:planetary-system-autocomplete')
    )

    class Meta:
        model = PlanetarySystems
        fields = ['name',]
