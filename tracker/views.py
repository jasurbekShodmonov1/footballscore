from django.shortcuts import render
from .models import Team, Match


# Create your views here.def dream_team(request):

def team_list(request):
    teams = Team.objects.all()
    return render(request,'team_list.html', {'teams': teams})


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})