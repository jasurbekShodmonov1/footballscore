from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team_list, name='team_list'),
    path('team/add/', views.add_team, name='add_team'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('matches/', views.match_list, name='match_list'),
    path('matches/add/', views.add_match, name='add_match'),
]
