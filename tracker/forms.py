from django import forms
from .models import Team, Match


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'logo']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'date', 'home_score', 'away_team']
