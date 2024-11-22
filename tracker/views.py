from django.shortcuts import render, get_object_or_404, redirect

from .forms import TeamForm, MatchForm
from .models import Team, Match


# Create your views here.def dream_team(request):

def team_list(request):
    teams = Team.objects.all()
    return render(request,'team_list.html', {'teams': teams})


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})


def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('team_list')
    else:
        form = TeamForm()
    return render(request, 'add_team.html',{'form': form})


def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'add_match.html', {'form': form})
